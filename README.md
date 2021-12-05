# Pokemon As A Service

Pokemon as a service allow you to store and retrieve pokemons<br/>
You can retrieve pokemons by their ID or by prefix search, for a<br/>
word in one of their field values

## API

| HTTP | URL                        | Action                                                                             |
| ---- | -------------------------- | ---------------------------------------------------------------------------------- |
| POST | /api/pokemon               | Store a pokemon by its pokadex_id                                                  |
| GET  | /api/pokemon/_id_          | Get pokemon by ID _id_                                                             |
| GET  | /api/pokemon               | Get all pokemons                                                                   |
| GET  | /api/autocomplete/_prefix_ | Get all pokemons that one of the words in their field values has a prefix _prefix_ |

## Maintenance

### Build once

```
docker-compose build
```

### Bring up the API

```
docker-compose up -d
```

### Bring down the API

```
docker-compose down
```

## API Examples

### Store a pokemon (by pokadex_id)

HTTP request:

```
POST /api/pokemon
{
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
```

Response:

```
{
    "pokemon": {
        "level": 60,
        "name": "Pikachu",
        "nickname": "Baruh Ha Gever",
        "pokadex_id": 25,
        "skills": [
            "Tail Whip",
            "Thunder Shock",
            "Growl",
            "Play Nice",
            "Quick Attack",
            "Electro Ball",
            "Thunder Wave"
        ],
        "type": "ELECTRIC"
    },
    "success": true
}
```

### Get pokemon by ID (pokadex_id)

HTTP request:

```
GET /api/pokemon/25
```

Response:

```
{
    "pokemon": {
        "level": 60,
        "name": "Pikachu",
        "nickname": "Baruh Ha Gever",
        "pokadex_id": 25,
        "skills": [
            "Tail Whip",
            "Thunder Shock",
            "Growl",
            "Play Nice",
            "Quick Attack",
            "Electro Ball",
            "Thunder Wave"
        ],
        "type": "ELECTRIC"
    },
    "success": true
}
```

### Get all pokemons

HTTP request:

```
GET /api/pokemon
```

Response:

```
{
    "pokemons": [
        {
            "level": 20,
            "name": "Bulbasaur",
            "nickname": "Gavrial",
            "pokadex_id": 1,
            "skills": [
                "Tackle",
                "Growl",
                "Vine Whip",
                "Poison Powder",
                "Sleep Powder",
                "Take Down",
                "Razor Leaf",
                "Growth"
            ],
            "type": "GRASS"
        },
        {
            "level": 60,
            "name": "Pikachu",
            "nickname": "Baruh Ha Gever",
            "pokadex_id": 25,
            "skills": [
                "Tail Whip",
                "Thunder Shock",
                "Growl",
                "Play Nice",
                "Quick Attack",
                "Electro Ball",
                "Thunder Wave"
            ],
            "type": "ELECTRIC"
        }
    ],
    "success": true
}
```

### Autocomplete: get pokemons by prefix (of some word in any field)

HTTP request:

```
GET /api/autocomplete/grow
```

Response:

```
{
    "pokemons": [
        {
            "level": 20,
            "name": "Bulbasaur",
            "nickname": "Gavrial",
            "pokadex_id": 1,
            "skills": [
                "Tackle",
                "Growl",
                "Vine Whip",
                "Poison Powder",
                "Sleep Powder",
                "Take Down",
                "Razor Leaf",
                "Growth"
            ],
            "type": "GRASS"
        },
        {
            "level": 60,
            "name": "Pikachu",
            "nickname": "Baruh Ha Gever",
            "pokadex_id": 25,
            "skills": [
                "Tail Whip",
                "Thunder Shock",
                "Growl",
                "Play Nice",
                "Quick Attack",
                "Electro Ball",
                "Thunder Wave"
            ],
            "type": "ELECTRIC"
        }
    ],
    "prefix": "grow",
    "success": true
}
```

Explanation: Both pokemons have a word that starts with 'grow' -<br/>
Bulbasaur has a 'Growth' skill, and<br/>
Pikachu has a 'Growl' skill
