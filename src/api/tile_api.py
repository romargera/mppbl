# src/api/tile_api.py
import requests
from ..config import API_KEY

def get_tile(x, y, z, lang="en_US", scale=1.5, projection="web_mercator"):
    base_url = "https://tiles.api.mappable.world/v1/tiles/"
    url = f"{base_url}?apikey={API_KEY}&lang={lang}&x={x}&y={y}&z={z}&l=map&scale={scale}&projection={projection}"
    response = requests.get(url)
    return response
