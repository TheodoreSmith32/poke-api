import psycopg2
from psycopg2 import pool

db_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=5,
    host="pg-pokemon",  # atau "postgres" kalau docker-compose
    database="pokemondb",
    user="admin",
    password="admin",
    port="5432"
)

def get_conn():
    return db_pool.getconn()

def release_conn(conn):
    db_pool.putconn(conn)