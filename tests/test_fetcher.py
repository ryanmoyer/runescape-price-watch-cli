import unittest

from mock import MagicMock, patch

import fetcher


@patch('requests.get')
class TestFetcher(unittest.TestCase):
    def test_integer_price(self, mock_get):
        mock_response = MagicMock()
        mock_response.json = {'item': {'name': 'maple logs', 'current': {'price': 12345}}}
        mock_get.return_value = mock_response
        self.assertEqual(fetcher.fetch_price(1517), ('maple logs', '12345'))
        mock_get.assert_called_once_with(
            'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=1517')

    def test_floating_point_price(self, mock_get):
        mock_response = MagicMock()
        mock_response.json = {'item': {'name': 'pickle', 'current': {'price': 1423.543}}}
        mock_get.return_value = mock_response
        self.assertEqual(fetcher.fetch_price(1234), ('pickle', '1423.543'))
        mock_get.assert_called_once_with(
            'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=1234')

    def test_comma_in_price(self, mock_get):
        mock_response = MagicMock()
        mock_response.json = {'item': {'name': 'fire rune', 'current': {'price': '345,821'}}}
        mock_get.return_value = mock_response
        self.assertEqual(fetcher.fetch_price(554), ('fire rune', '345,821'))
        mock_get.assert_called_once_with(
            'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=554')

    def test_k_at_end(self, mock_get):
        mock_response = MagicMock()
        mock_response.json = {'item': {'name': 'frost dragon bones', 'current': {'price': '123k'}}}
        mock_get.return_value = mock_response
        self.assertEqual(fetcher.fetch_price(1337), ('frost dragon bones', '123k'))
        mock_get.assert_called_once_with(
            'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=1337')


