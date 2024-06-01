# src/api/tile_api.py
import requests
import logging
from src.config import API_KEY

def get_tile(x, y, z, lang="en_US", scale=1.5, projection="web_mercator"):
    base_url = "https://tiles.api.mappable.world/v1/tiles/"
    url = f"{base_url}?apikey={API_KEY}&lang={lang}&x={x}&y={y}&z={z}&l=map&scale={scale}&projection={projection}"
    response = requests.get(url)
    logging.info(f"Requesting tile at zoom level {z} for coordinates ({x}, {y})")
    return response


# src/api/tile_api.py
import requests
from src.config import API_KEY
from .conversion import lat_lon_to_tile

def get_tile(lat, lon, zoom):
    x, y = lat_lon_to_tile(lat, lon, zoom)
    url = f"https://tiles.api.mappable.world/v1/tiles/?apikey={API_KEY}&x={x}&y={y}&z={zoom}"
    response = requests.get(url)
    return response
