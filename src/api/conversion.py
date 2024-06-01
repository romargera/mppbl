# src/api/conversion.py
import math

import math


def lat_lon_to_tile_numbers(lat, lon, zoom):
    """
    Convert latitude and longitude to tile x, y coordinates based on the zoom level.
    This function uses the Web Mercator projection to calculate tile numbers.

    :param lat: Latitude in degrees.
    :param lon: Longitude in degrees.
    :param zoom: Zoom level.
    :return: (x_tile, y_tile) Tile coordinates.
    """
    lat_rad = math.radians(lat)
    # Calculate global pixel coordinates
    x = (lon + 180.0) / 360.0 * (2 ** zoom * 256)
    y = (1 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * (2 ** zoom * 256)

    # Calculate global pixel coordinates
    p = (2 ^ (zoom + 8)) / 2

    x = p * ((lon / 180) + 1)

    ln = math.log(  )
    y = p * ( 1 - (ln / math.pi ))



         / 360.0 * (2 ** zoom * 256))
    y = (1 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * (2 ** zoom * 256)


    # Convert pixel coordinates to tile numbers
    x_tile = int(x // 256)
    y_tile = int(y // 256)
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
        (central_tile[0], central_tile[1] - 1),  # top-center
        (central_tile[0] + 1, central_tile[1] - 1),  # top-right
        (central_tile[0] - 1, central_tile[1]),  # center-left
        central_tile,  # center
        (central_tile[0] + 1, central_tile[1]),  # center-right
        (central_tile[0] - 1, central_tile[1] + 1),  # bottom-left
        (central_tile[0], central_tile[1] + 1),  # bottom-center
        (central_tile[0] + 1, central_tile[1] + 1)  # bottom-right
    ]
    return tiles

