import requests
import math
from dotenv import load_dotenv
import os

load_dotenv()  # This loads the environment variables from .env

# Set up the endpoint and required parameters
api_key = os.getenv("api_key")
base_url = "https://tiles.api.mappable.world/v1/tiles/"
lang = "en_US"
lat, lon = 41.025658, 28.974155  # Galata Tower coordinates
z = 16
l = "map"

def lat_lon_to_tile_numbers(lat, lon, zoom):
    # Convert latitude and longitude to pixel coordinates
    lat_rad = math.radians(lat)
    n = 2.0 ** zoom
    x_tile = int((lon + 180.0) / 360.0 * n)
    y_tile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return (x_tile, y_tile)

# Calculate central tile
central_tile = lat_lon_to_tile_numbers(lat, lon, z)
tiles = [
    (central_tile[0] - 1, central_tile[1] - 1),  # top-left
    (central_tile[0], central_tile[1] - 1),      # top-right
    (central_tile[0] - 1, central_tile[1]),      # bottom-left
    central_tile                                 # bottom-right
]

# Optional parameters
scale = 1.5
projection = "web_mercator"

# Request tiles
for x_tile, y_tile in tiles:
    full_url = f"{base_url}?apikey={api_key}&lang={lang}&x={x_tile}&y={y_tile}&z={z}&l={l}&scale={scale}&projection={projection}"
    response = requests.get(full_url)
    if response.status_code == 200:
        print("Request successful for tile (x={}, y={})".format(x_tile, y_tile))
    else:
        print(f"Failed to retrieve data for tile (x={x_tile}, y={y_tile}): {response.status_code}")
    print("URL Requested:", full_url)
