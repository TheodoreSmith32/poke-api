from fastapi import FastAPI,HTTPException,Body
from jsonschema import validate, ValidationError
import requests

from schemas.schema import item_schema, template_post
from schemas.pokemon_schema import pokemon_request_schema , pokemon_request_example
from data_processing.insert_pg import insert_pokemon_ability
from data_processing.create_table import create_table


app = FastAPI(
    title="Poke API Service",
    description="API get Pokemon Ability",
    version="0.1"
)

items = []

#Create Table Postgre
create_table()


# LIST API 
@app.get("/")
def root():
    return {"message": "Hello from Docker FastAPI"}

#get items from list items
@app.get("/poke-api/v1/get_items")
def get_all_items():
    return items

#create item
# @app.post("/items")
# def create_item(item: dict):
#     items.append(item)
#     return {"message": "Item added", "data": item}

#API Item
@app.post("/poke-api/v1/items_with_schema")
def create_random_item(item: dict = Body(..., example=template_post)):
    #validate JSON schema
    try:
        validate(instance=item, schema=item_schema)
    except ValidationError as e:
        raise HTTPException(
            status_code=400,
            detail=e.message
        )

    items.append(item)
    return {
        "message": "Item valid & added",
        "data": item
    }


#API Pokemon
@app.post("/poke-api/v1/pokemon-ability")
def get_pokemon_ability_insert_to_db(
    data: dict = Body(..., example=pokemon_request_example)
):
    try:
        validate(instance=data, schema=pokemon_request_schema)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.message)

    ability_id = data["pokemon_ability_id"]


    # call PokeAPI
    url = f"https://pokeapi.co/api/v2/ability/{ability_id}"
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Ability not found")

    res = response.json()

    # ambil entries (filter en & de)
    returned_entries = [
        {
            "effect": e["effect"],
            "language": e["language"],
            "short_effect": e["short_effect"]
        }
        for e in res.get("effect_entries", [])
        if e["language"]["name"] in ["en", "de"]
    ]


    #pokemon list
    pokemon_list = [
        p["pokemon"]["name"]
        for p in res.get("pokemon", [])
    ]
    
    result = {
        "raw_id": data["raw_id"],
        "user_id": data["user_id"],
        "returned_entries": returned_entries,
        "pokemon_list": pokemon_list
    }
    #insert to db
    insert_pokemon_ability(data, returned_entries)
    items.append(result)
    return result
    