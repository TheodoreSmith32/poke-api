
item_schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "minLength": 1
        },
        "price": {
            "type": "number",
            "minimum": 0
        },
        "notes":{
            "type": "string"
        }
    },
    "required": ["name", "price"],  
    "additionalProperties": False   
}

template_post = {
    "name": "Laptop",
    "price": 10000,
    "notes" : "Ini adalah Laptop Gaming"
}