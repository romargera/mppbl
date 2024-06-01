# src/main.py
from dotenv import load_dotenv
from src.api.tile_api import get_tile
from src.database import create_connection, create_table, insert_api_request

def main():
    load_dotenv()  # Load environment variables

    # Database setup
    conn = create_connection()
    create_table(conn)

    # Example API request
    response = get_tile(42830, 28025, 16)
    if response.ok:
        print("Tile retrieved successfully.")
        insert_api_request(conn, response.text, 41.025658, 28.974155, 42830, 28025, response.url)
    else:
        print("Failed to retrieve tile.")

    conn.close()

if __name__ == "__main__":
    main()
