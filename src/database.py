# src/database.py
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('api_requests.db')
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS api_requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
                request TEXT,
                lat REAL,
                lon REAL,
                x INTEGER,
                y INTEGER,
                full_url TEXT
            );
        """)
    except Error as e:
        print(e)

def insert_api_request(conn, request, lat, lon, x, y, full_url):
    sql = ''' INSERT INTO api_requests(request, lat, lon, x, y, full_url)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (request, lat, lon, x, y, full_url))
    conn.commit()
