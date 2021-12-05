from flask import Flask, request
from pokemon import validate_pokemon, Pokemon
from elasticsearch import Elasticsearch
from flask_caching import Cache

ES_POKEMONS_INDEX = 'pokemons'
CACHE_LIFETIME_IN_SECONDS = 15

app = Flask(__name__)
app.config.from_object('config.Config')
cache = Cache(app)
es = Elasticsearch(app.config.get('ES_HOST_NAME'))


@app.route('/')
def home():
    return 'Pokemon as a service home'


@app.route('/api/pokemon', methods=['POST'])
def index_pokemon():
    global es
    try:
        pokemon = validate_pokemon(request.json)
        id = pokemon[Pokemon.ID_FIELD_NAME]
        es.index(index=ES_POKEMONS_INDEX, id=id, document=pokemon)
        return {
            'pokemon': pokemon,
            'success': True
        }
    except Exception as e:
        return {
            'error': str(e),
            'success': False,
        }


@app.route('/api/pokemon')
@cache.cached(timeout=CACHE_LIFETIME_IN_SECONDS, query_string=True)
def get_pokemons():
    global es
    try:
        query = {
            'match_all': {}
        }
        es_response = es.search(index=ES_POKEMONS_INDEX, query=query)
        pokemons = _extract_pokemons(es_response)
        return {
            'pokemons': pokemons,
            'success': True,
        }
    except Exception as e:
        return {
            'error:': str(e),
            'success': False,
        }


@app.route('/api/pokemon/<id>')
@cache.cached(timeout=CACHE_LIFETIME_IN_SECONDS, query_string=True)
def get_pokemon(id):
    global es
    try:
        query = {
            'match': {
                Pokemon.ID_FIELD_NAME: id
            }
        }
        es_response = es.search(index=ES_POKEMONS_INDEX, query=query)
        pokemons = _extract_pokemons(es_response)
        if not pokemons:
            raise f'Cannot find pokemon with ID {id}'
        return {
            'pokemon': pokemons[0],
            'success': True,
        }
    except Exception as e:
        return {
            'error:': str(e),
            'success': False,
        }


@ app.route('/api/autocomplete/<prefix>')
@cache.cached(timeout=CACHE_LIFETIME_IN_SECONDS, query_string=True)
def autocomplete(prefix):
    global es
    try:
        query = {
            'multi_match': {
                'type': 'phrase_prefix',
                'query': prefix,
                'fields': ['*'],
            }
        }
        es_response = es.search(index=ES_POKEMONS_INDEX, query=query)
        pokemons = _extract_pokemons(es_response)
        return {
            'prefix': prefix,
            'pokemons': pokemons,
            'success': True
        }
    except Exception as e:
        return {
            'error': str(e),
            'success': False,
        }


def _extract_pokemons(es_response):
    ''' Extracts pokemons from elasticsearch search query response '''
    es_pokemons = es_response['hits']['hits']
    return [p['_source'] for p in es_pokemons]
