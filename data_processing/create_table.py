from connection.postgres import get_conn, release_conn

def create_table():
    conn = get_conn()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pokemon_abilities (
                id SERIAL PRIMARY KEY,
                raw_id TEXT,
                user_id TEXT,
                pokemon_ability_id INT,
                effect TEXT,
                language JSONB,
                short_effect TEXT
            );
        """)
        conn.commit()
        print("Table created / already exists")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        cursor.close()
        release_conn(conn)