from flask import Flask, request, Response, jsonify
from pokemon import Pokemon
import json

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello world!'


@app.route('/', methods=['POST'])
def index_pokemon():
    try:
        pokemon = Pokemon(**request.json)
        return {
            'response': pokemon.asdict()
        }
    except Exception as e:
        return {
            'error': str(e)
        }


@app.route('/api/autocomplete/<pattern>')
def autocomplete(pattern):
    return {
        'pattern': pattern
    }


pokemon1 = {
    "pokadex_id": 25,
    "name": "Pikachu",
    "nickname": "Baruh Ha Gever",
    "level": 60,
    "type": "ELECTRIC",
    "skills": [
        "Tail Whip",
        "Thunder Shock",
        "Growl",
        "Play Nice",
        "Quick Attack",
        "Electro Ball",
        "Thunder Wave"
    ]
}
