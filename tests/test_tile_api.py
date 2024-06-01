import unittest
from unittest.mock import patch
from src.api.tile_api import get_tile

class TestTileAPI(unittest.TestCase):
    @patch('src.api.tile_api.requests.get')
    def test_get_tile_success(self, mock_get):
        # Configure the mock to return a response with a 200 status code
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'Success'

        response = get_tile(10, 10, 5)
        self.assertEqual(response.status_code, 200)

    @patch('src.api.tile_api.requests.get')
    def test_get_tile_content(self, mock_get):
        # Configure the mock to return a response with a 403 status code and specific text
        mock_get.return_value.status_code = 403
        mock_get.return_value.text = 'Invalid key'

        response = get_tile(10, 10, 5)
        self.assertEqual(response.status_code, 403)
        self.assertIn('Invalid key', response.text)

if __name__ == '__main__':
    unittest.main()
