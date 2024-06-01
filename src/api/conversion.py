# src/api/conversion.py

import math
from src.config import lat, lon, zoom, projection, scale


# def lat_lon_to_tile_numbers(lat, lon, zoom):
#     """
#     Convert latitude and longitude to tile x, y coordinates based on the zoom level.
#     This function uses the Web Mercator projection to calculate tile numbers.
#
#     :param lat: Latitude in degrees.
#     :param lon: Longitude in degrees.
#     :param zoom: Zoom level.
#     :return: (x_tile, y_tile) Tile coordinates.
#     """
#     # print(lat, lon)
#     # Calculate global pixel coordinates
#     lat = math.radians(lat)
#     lon = math.radians(lon)
#     # Constants
#     epsilon = 0.0818191908426
#
#     # Convert latitude to radians and calculate beta
#     beta = int (math.pi * lat) / 180
#
#     # Calculate phi
#     phi = (1 - epsilon * math.sin(beta)) / (1 + epsilon * math.sin(beta))
#     phi_0 = phi ** (epsilon / 2)
#
#     # Calculate theta
#     theta = math.tan(math.pi / 4 + beta / 2) * phi_0
#
#     # Calculate rho, where 'zoom' is scaled by 8 (z*8)
#     rho = (2 ** (zoom + 8)) / 2
#
#     # Calculate global pixel coordinates
#     x_p = rho * int (1 + lon / 180)
#     y_p = rho * (1 - math.log(theta) / math.pi)
#
#     # print(x_p, y_p)
#
#     # Convert pixel coordinates to tile numbers
#     x_tile = math.floor(x_p / 256)
#     y_tile = math.floor(y_p / 256)
#     # print(x_tile, y_tile)
#     return x_tile, y_tile

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






# # # Пример использования
# lat = 25.19745
# lon = 55.27417
# zoom = 16
#
# x_p, y_p = lat_lon_to_tile_numbers(lat, lon, zoom)
# print(x_p, y_p)

# 25.19745, 55.27417, 16 >>> should be  x=42830&y=28025
