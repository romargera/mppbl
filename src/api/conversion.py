# src/api/conversion.py

import math
from src.config import lat, lon, zoom, projection, scale

def lat_lon_to_tile_numbers(lat, lon, zoom):
    # Convert latitude and longitude to pixel coordinates
    lat_rad = math.radians(lat)
    n = 2.0 ** zoom
    x_tile = int((lon + 180.0) / 360.0 * n)
    y_tile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return [
        (x_tile - 1, y_tile - 1),  # top-left
        (x_tile, y_tile - 1),      # top-right
        (x_tile - 1, y_tile),      # bottom-left
        (x_tile, y_tile)           # central
    ]

# Calculate central tile
# central_tile = lat_lon_to_tile_numbers(lat, lon, zoom)
# # 4 tiles
# tiles = [
#     (central_tile[0] - 1, central_tile[1] - 1),  # top-left
#     (central_tile[0], central_tile[1] - 1),      # top-right
#     (central_tile[0] - 1, central_tile[1]),      # bottom-left
#     central_tile                                 # bottom-right
# ]

# def get_tiles(lat, lon, zoom):
#     tiles = [
#         (lat - 0.01, lon - 0.01),  # Adjust the calculation based on your actual grid/logic
#         (lat, lon - 0.01),
#         (lat - 0.01, lon),
#         (lat, lon)
#     ]
#     results = []
#     for index, (lat, lon) in enumerate(tiles, start=1):
#         response, x, y, url = get_tile(lat, lon, zoom)  # Assume get_tile exists and fetches data
#         results.append((index, response, x, y, url))
#     return results


# src/api/tile_api.py
def get_tiles(lat, lon, zoom):
    try:
        tiles = lat_lon_to_tile_numbers(lat, lon, zoom)
        results = []
        for x, y in tiles:
            url = f"http://tileserver.com/tiles?x={x}&y={y}&z={zoom}"
            response = requests.get(url)
            if response.ok:
                results.append((response, x, y, url))
            else:
                logging.error(f"Failed to retrieve tile at {x}, {y}")
        return results
    except Exception as e:
        logging.error(f"An error occurred while fetching tiles: {str(e)}")
