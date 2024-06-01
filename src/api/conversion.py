# src/api/conversion.py

import math
from src.config import lat, lon, zoom, projection, scale

def lat_lon_to_tile_numbers(lat, lon, zoom):
    # Convert latitude and longitude to pixel coordinates
    lat_rad = math.radians(lat)
    n = 2.0 ** zoom
    x_tile = int((lon + 180.0) / 360.0 * n)
    y_tile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return (x_tile, y_tile)

# Calculate central tile
central_tile = lat_lon_to_tile_numbers(lat, lon, zoom)
# 4 tiles
tiles = [
    (central_tile[0] - 1, central_tile[1] - 1),  # top-left
    (central_tile[0], central_tile[1] - 1),      # top-right
    (central_tile[0] - 1, central_tile[1]),      # bottom-left
    central_tile                                 # bottom-right
]
