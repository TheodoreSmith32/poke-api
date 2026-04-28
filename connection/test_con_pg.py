import psycopg2

def test_connection():
    try:
        conn = psycopg2.connect(
            host="postgres",      # 👈 kalau pakai docker-compose
            database="pokemondb",
            user="admin",
            password="admin",
            port="5432"
        )

        cursor = conn.cursor()

        # test query sederhana
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()

        print("✅ Connected to PostgreSQL!")
        print("Version:", db_version)

        cursor.close()
        conn.close()

    except Exception as e:
        print("❌ Connection failed")
        print(str(e))


if __name__ == "__main__":
    test_connection()