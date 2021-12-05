# Pokemon As A Service

## Build once

```
docker-compose build
```

## Run

```
docker-compose up
```

# API

## Index a pokemon

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

## Get pokemon by ID (pokadex_id)

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

## Get all pokemons

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

## Autocomplete: get pokemons by prefix (of any word in any field)

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
