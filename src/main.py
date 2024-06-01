# src/main.py
import os
import logging
from dotenv import load_dotenv
from src.database import create_connection, create_table, insert_api_request
from src.api.tile_api import get_tile

def setup_logging():
    logs_directory = os.path.join(os.path.dirname(__file__), '..', 'logs')
    os.makedirs(logs_directory, exist_ok=True)  # Ensure the directory exists
    log_file_path = os.path.join(logs_directory, 'app.log')
    logging.basicConfig(filename=log_file_path, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    load_dotenv()  # Load environment variables
    setup_logging()
    conn = create_connection()
    create_table(conn)

    # Example data
    lat, lon, zoom = 48.5129, 2.1740, 13  # Replace with real data

    response, x, y, url = get_tile(lat, lon, zoom)
    if response.ok:
        logging.info("Tile retrieved successfully.")
        insert_api_request(conn, response.text, lat, lon, x, y, url)
    else:
        logging.error("Failed to retrieve tile.")

    conn.close()

if __name__ == "__main__":
    main()
