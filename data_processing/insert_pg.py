import json
from connection.postgres import get_conn, release_conn

def insert_pokemon_ability(data, returned_entries):
    conn = get_conn()
    cursor = conn.cursor()

    try:
        for entry in returned_entries:
            cursor.execute(
                """
                INSERT INTO pokemon_abilities 
                (raw_id, user_id, pokemon_ability_id, effect, language, short_effect)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    data["raw_id"],
                    data["user_id"],
                    int(data["pokemon_ability_id"]),
                    entry["effect"],
                    json.dumps(entry["language"]),
                    entry["short_effect"]
                )
            )

        conn.commit()

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        cursor.close()
        release_conn(conn)