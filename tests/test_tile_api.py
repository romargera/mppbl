# src/tests/test_tile_api.py
import unittest
from unittest.mock import patch
from src.api.tile_api import get_tile
from src.config import API_KEY

class TestTileAPI(unittest.TestCase):
    @patch('src.api.tile_api.requests.get')
    def test_get_tile_successful(self, mock_get):
        """Test the get_tile function returns a successful response."""
        # Setup mock
        mock_response = mock_get.return_value
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.text = 'Successful response'
        mock_response.url = 'https://tiles.api.mappable.world/v1/tiles/?x=42830&y=28025&z=16&lang=en_US&l=map&apikey=API_KEY'

        # Expected values
        expected_x, expected_y = 42830, 28025

        # Call the function
        response, x, y, url = get_tile(41.025658, 28.974155, 16)

        # Assertions to ensure all returned values match expected values
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Successful response', response.text)
        self.assertEqual(x, expected_x)
        self.assertEqual(y, expected_y)
        self.assertIn('apikey=API_KEY', url)

    @patch('src.api.tile_api.requests.get')
    def test_get_tile_failure(self, mock_get):
        """Test the get_tile function handles failures correctly."""
        # Setup mock
        mock_response = mock_get.return_value
        mock_response.ok = False
        mock_response.status_code = 400
        mock_response.text = '"l" is required'
        mock_response.url = 'https://tiles.api.mappable.world/v1/tiles/'

        # Call the function
        response, x, y, url = get_tile(41.025658, 28.974155, 16)

        # Assertions
        self.assertFalse(response.ok)
        self.assertEqual(response.status_code, 400)
        self.assertIn('"l" is required', response.text)

if __name__ == '__main__':
    unittest.main()
