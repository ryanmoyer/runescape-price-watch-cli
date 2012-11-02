import unittest

from mock import MagicMock, patch

import fetcher


@patch('requests.get')
class TestFetcher(unittest.TestCase):
    def test_integer_price(self, mock_get):
        mock_response = MagicMock()
        mock_response.json = {'item': {'current': {'price': 12345}}}
        mock_get.return_value = mock_response
        self.assertEqual(fetcher.fetch_price(1517), '12345')
        mock_get.assert_called_once_with(
            'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=1517')

    def test_floating_point_price(self, mock_get):
        mock_response = MagicMock()
        mock_response.json = {'item': {'current': {'price': 1423.543}}}
        mock_get.return_value = mock_response
        self.assertEqual(fetcher.fetch_price(1234), '1423.543')
        mock_get.assert_called_once_with(
            'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=1234')

    def test_comma_in_price(self, mock_get):
        mock_response = MagicMock()
        mock_response.json = {'item': {'current': {'price': '345,821'}}}
        mock_get.return_value = mock_response
        self.assertEqual(fetcher.fetch_price(554), '345,821')
        mock_get.assert_called_once_with(
            'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=554')

    def test_k_at_end(self, mock_get):
        mock_response = MagicMock()
        mock_response.json = {'item': {'current': {'price': '123k'}}}
        mock_get.return_value = mock_response
        self.assertEqual(fetcher.fetch_price(1337), '123k')
        mock_get.assert_called_once_with(
            'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=1337')
