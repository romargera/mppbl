# import os
# import logging
# from dotenv import load_dotenv
# from src.database import create_connection, create_table, insert_api_request
# from src.api.tile_api import get_tiles, setup_logging
# from src.config import lat, lon, zoom
#
# def main():
#     load_dotenv()  # Load environment variables
#     setup_logging()
#
#     conn = create_connection()
#     create_table(conn)
#
#     tile_coordinates = [(lat, lon)]  # Example list of tile coordinates
#     results = get_tiles(tile_coordinates, zoom)
#
#     for index, response, x, y, url in results:
#         if response.ok:
#             logging.info(f"Tile {index} retrieved successfully.")
#             insert_api_request(conn, response.text, lat, lon, x, y, url, response.status_code)
#         else:
#             logging.error(f"Failed to retrieve tile {index}. Status: {response.status_code}")
#
#     conn.close()
#
# if __name__ == "__main__":
#     main()
import logging
from src.api.tile_api import get_tiles
from src.config import lat, lon, zoom
from src.database import create_connection, create_table, insert_api_request
from src.config import API_KEY, projection, scale, l  # Ensure these are correctly defined in config.py

# Setup logging
def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Main execution function
def main():
    setup_logging()
    logging.info("Starting the application")

    # Database setup
    conn = create_connection()
    create_table(conn)

    # Coordinates for the central tile
    # lat, lon, zoom = 25.19745, 55.27417, 10  # Example coordinates and zoom level

    # Fetch tiles
    try:
        tiles = get_tiles(lat, lon, zoom)
        for index, response, x, y, url in tiles:
            if response.ok:
                logging.info(f"Tile {index} retrieved successfully at {x}, {y}.")
                insert_api_request(conn, response.text, lat, lon, x, y, url, response.status_code)
            else:
                logging.error(f"Failed to retrieve tile {index} at {x}, {y}. Status Code: {response.status_code}")
    except Exception as e:
        logging.error(f"An error occurred while fetching tiles: {str(e)}")

    # Close the database connection
    if conn:
        conn.close()
        logging.info("Database connection closed")

if __name__ == "__main__":
    main()
