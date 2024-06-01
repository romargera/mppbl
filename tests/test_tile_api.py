import unittest
from unittest.mock import patch, MagicMock
from src.api.tile_api import get_tile, get_tiles


class TestTileAPI(unittest.TestCase):
    def setUp(self):
        # This method will run before each test method
        self.mock_response = MagicMock()
        self.mock_response.ok = True
        self.mock_response.status_code = 200
        self.mock_response.text = 'Success'

    @patch('src.api.tile_api.requests.get')
    def test_get_tile_successful(self, mock_get):
        """Test successful retrieval of a tile."""
        mock_get.return_value = self.mock_response
        # Define test parameters
        lat, lon, zoom = 25.19745, 55.27417, 10
        # Execute function under test
        response, x, y, url = get_tile(lat, lon, zoom)
        # Assertions to verify expected outcomes
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Success')

    @patch('src.api.tile_api.get_tile')
    def test_get_tiles(self, mock_get_tile):
        """Test retrieving multiple tiles."""
        # Setup mock for get_tile
        mock_get_tile.return_value = (self.mock_response, 42830, 28025, 'mock_url')
        # Define test parameters
        tiles = [(25.19745, 55.27417), (25.19745, 55.27417)]  # Multiple coordinates
        zoom = 10
        # Execute function under test
        results = get_tiles(tiles, zoom)
        # Assertions to verify expected outcomes
        self.assertEqual(len(results), len(tiles))
        for result in results:
            index, response, x, y, url = result
            self.assertTrue(response.ok)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(x, 42830)
            self.assertEqual(y, 28025)

if __name__ == '__main__':
    unittest.main()
