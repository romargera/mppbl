# src/api/tile_api.py
import requests
import logging
from src.config import API_KEY, lat, lon, zoom, projection, scale, l
from src.api.conversion import lat_lon_to_tile_numbers  # Corrected import statement

def get_tile(lat, lon, zoom):
    x, y = lat_lon_to_tile_numbers(lat, lon, zoom)  # Corrected function call
    lang = "en_US"
    url = (f"https://tiles.api.mappable.world/v1/tiles/?x={x}&y={y}&z={zoom}&lang={lang}&l={l}&scale={scale}"
           f"&projection={projection}&apikey={API_KEY}")
    response = requests.get(url)
    logging.info(f"Requested URL: {url} - Status Code: {response.status_code}")
    if not response.ok:
        logging.error(f"Failed to retrieve tile. Status Code: {response.status_code}, Response: {response.text}")
    # print(lat, lon, zoom, x, y)
    return response, x, y, url

# for x_tile, y_tile in tiles:
#     full_url = f"{base_url}?apikey={api_key}&lang={lang}&x={x_tile}&y={y_tile}&z={z}&l={l}&scale={scale}&projection={projection}"
#     response = requests.get(full_url)
#     if response.status_code == 200:
#         print("Request successful for tile (x={}, y={})".format(x_tile, y_tile))
#     else:
#         print(f"Failed to retrieve data for tile (x={x_tile}, y={y_tile}): {response.status_code}")
#     print("URL Requested:", full_url)