import os
import logging
from dotenv import load_dotenv
from src.database import create_connection, create_table, insert_api_request
from src.api.tile_api import get_tiles, setup_logging
from src.config import lat, lon, zoom

def main():
    load_dotenv()  # Load environment variables
    setup_logging()

    conn = create_connection()
    create_table(conn)

    tile_coordinates = [(lat, lon)]  # Example list of tile coordinates
    results = get_tiles(tile_coordinates, zoom)

    for index, response, x, y, url in results:
        if response.ok:
            logging.info(f"Tile {index} retrieved successfully.")
            insert_api_request(conn, response.text, lat, lon, x, y, url, response.status_code)
        else:
            logging.error(f"Failed to retrieve tile {index}. Status: {response.status_code}")

    conn.close()

if __name__ == "__main__":
    main()
