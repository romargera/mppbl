# src/api/tile_api.py
import requests
import logging
from src.config import API_KEY
from src.api.conversion import lat_lon_to_tile_numbers  # Corrected import statement

def get_tile(lat, lon, zoom):
    x, y = lat_lon_to_tile_numbers(lat, lon, zoom)  # Corrected function call
    lang = "en_US"
    layer = "map"
    url = f"https://tiles.api.mappable.world/v1/tiles/?x={x}&y={y}&z={zoom}&lang={lang}&l={layer}&apikey={API_KEY}"
    response = requests.get(url)
    logging.info(f"Requested URL: {url} - Status Code: {response.status_code}")
    if not response.ok:
        logging.error(f"Failed to retrieve tile. Status Code: {response.status_code}, Response: {response.text}")
    return response, x, y, url
