# src/main.py
import os
import logging
from dotenv import load_dotenv
from src.database import create_connection, create_table, insert_api_request
from src.api.tile_api import get_tile
from src.config import lat, lon, zoom
from src.api.conversion import tiles

# Example data
# # lat, lon, zoom = 48.858653170975046, 2.294514165895997, 10  # Replace with real data
#
# def setup_logging():
#     logs_directory = os.path.join(os.path.dirname(__file__), '..', 'logs')
#     os.makedirs(logs_directory, exist_ok=True)  # Ensure the directory exists
#     log_file_path = os.path.join(logs_directory, 'app.log')
#     logging.basicConfig(filename=log_file_path, level=logging.INFO,
#                         format='%(asctime)s:%(levelname)s:%(message)s')
#
# def main():
#     load_dotenv()  # Load environment variables
#     setup_logging()
#     conn = create_connection()
#     create_table(conn)
#
#     response, x, y, url = get_tile(lat, lon, zoom)
#     if response.ok:
#         logging.info("Tile retrieved successfully.")
#         insert_api_request(conn, response.text, lat, lon, x, y, url)
#     else:
#         logging.error("Failed to retrieve tile.")
#
#     conn.close()
#
# if __name__ == "__main__":
#     main()


# for x_tile, y_tile in tiles:
#     full_url = f"{base_url}?apikey={api_key}&lang={lang}&x={x_tile}&y={y_tile}&z={z}&l={l}&scale={scale}&projection={projection}"
#     response = requests.get(full_url)
#     if response.status_code == 200:
#         print("Request successful for tile (x={}, y={})".format(x_tile, y_tile))
#     else:
#         print(f"Failed to retrieve data for tile (x={x_tile}, y={y_tile}): {response.status_code}")
#     print("URL Requested:", full_url)