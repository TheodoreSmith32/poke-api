pokemon_request_schema = {
    "type": "object",
    "properties": {
        "raw_id": {"type": "string",            
                   "minLength": 13,
                   "maxLength": 13,
                   },
        "user_id": {"type": "string",
                    "minLength": 7,
                     "maxLength": 7,
                     "pattern": "^[0-9]{7}$" 
                    },
        "pokemon_ability_id": {"type": "string"}
    },
    "required": ["raw_id", "user_id", "pokemon_ability_id"],
    "additionalProperties": False
}

pokemon_request_example = {
    "raw_id": "7dsa8d7sa9dsa",
    "user_id": "5199434",
    "pokemon_ability_id": "150"
}