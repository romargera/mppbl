import requests
import logging
from src.config import API_KEY, projection, scale, l

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log')

def get_tile(lat, lon, zoom):
    from src.api.conversion import lat_lon_to_tile_numbers
    x, y = lat_lon_to_tile_numbers(lat, lon, zoom)
    url = (f"https://tiles.api.mappable.world/v1/tiles/?x={x}&y={y}&z={zoom}&lang=en_US&l={l}&scale={scale}&projection="
           f"{projection}&apikey={API_KEY}")
    response = requests.get(url)
    logging.info(f"Requested URL: {url} - Status Code: {response.status_code}")
    return response, x, y, url

def get_tiles(tiles, zoom):
    results = []
    for index, (lat, lon) in enumerate(tiles, start=1):
        response, x, y, url = get_tile(lat, lon, zoom)
        results.append((index, response, x, y, url))
        logging.info(f"Tile number {index}: x={x}, y={y}, url={url}, status={response.status_code}")
    return results

