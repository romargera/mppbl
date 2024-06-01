# src/api/conversion.py
import math

def lat_lon_to_tile_numbers(lat, lon, zoom):
    """
    Convert latitude and longitude to tile x, y coordinates based on the zoom level.
    This uses the Web Mercator projection to calculate tile numbers.

    :param lat: Latitude in degrees.
    :param lon: Longitude in degrees.
    :param zoom: Zoom level.
    :return: (x_tile, y_tile) Tile coordinates.
    """
    lat_rad = math.radians(lat)
    n = 2.0 ** zoom
    x_tile = int((lon + 180.0) / 360.0 * n)
    y_tile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return x_tile, y_tile

def calculate_tiles(lat, lon, zoom):
    """
    Calculate the central tile and adjacent tiles based on the provided latitude,
    longitude, and zoom level.

    :param lat: Latitude in degrees.
    :param lon: Longitude in degrees.
    :param zoom: Zoom level.
    :return: A list of tuples representing the x, y coordinates of the central and adjacent tiles.
    """
    central_tile = lat_lon_to_tile_numbers(lat, lon, zoom)
    tiles = [
        (central_tile[0] - 1, central_tile[1] - 1),  # top-left
        (central_tile[0], central_tile[1] - 1),      # top-right
        (central_tile[0] - 1, central_tile[1]),      # bottom-left
        central_tile                                 # bottom-right
    ]
    return tiles

# Additional example use-case
# lat, lon, z = 41.0256, 28.9741, 16  # Example coordinates for testing
# tiles = calculate_tiles(lat, lon, z)
# print("Calculated tiles:", tiles)
