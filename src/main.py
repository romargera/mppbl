# src/main.py
from api.tile_api import get_tile

def main():
    # Example function call
    response = get_tile(42830, 28025, 16)
    if response.ok:
        print("Tile retrieved successfully.")
    else:
        print("Failed to retrieve tile.")

if __name__ == "__main__":
    main()
