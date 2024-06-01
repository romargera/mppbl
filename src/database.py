import sqlite3
import logging

def create_connection():
    try:
        conn = sqlite3.connect('tiles.db')
        logging.info("Connection to SQLite DB successful")
        return conn
    except sqlite3.Error as e:
        logging.error(f"Error '{e}' occurred while connecting to SQLite DB")
        return None

def create_table(conn):
    if conn is not None:
        create_table_sql = '''
        CREATE TABLE IF NOT EXISTS tiles (
            tile_number INTEGER PRIMARY KEY AUTOINCREMENT,
            response_text TEXT,
            lat REAL,
            lon REAL,
            x_tile INTEGER,
            y_tile INTEGER,
            url TEXT,
            status_code INTEGER
        );
        '''
        try:
            cur = conn.cursor()
            cur.execute(create_table_sql)
            conn.commit()
            logging.info("SQLite table created successfully")
        except sqlite3.Error as e:
            logging.error(f"Error '{e}' occurred while creating the table")

def insert_api_request(conn, response_text, lat, lon, x, y, url, status_code):
    if conn is not None:
        sql = '''
        INSERT INTO tiles (response_text, lat, lon, x_tile, y_tile, url, status_code)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        try:
            cur = conn.cursor()
            cur.execute(sql, (response_text, lat, lon, x, y, url, status_code))
            conn.commit()
            logging.info("API request logged successfully")
        except sqlite3.Error as e:
            logging.error(f"Error '{e}' occurred while inserting into the table")
