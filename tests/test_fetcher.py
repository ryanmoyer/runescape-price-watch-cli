import unittest

from mock import MagicMock, patch

import fetcher


@patch('requests.get')
class TestFetcher(unittest.TestCase):
    def test_maple_logs(self, mock_get):
        mock_response = MagicMock()
        mock_response.json = {'item': {'current': {'price': 12345}}}
        mock_get.return_value = mock_response
        self.assertEqual(fetcher.fetch_price(1517), 12345)
        mock_get.assert_called_once_with('http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=1517')

    def test_fire_rune(self, mock_get):
        mock_response = MagicMock()
        mock_response.json = {'item': {'current': {'price': 54321}}}
        mock_get.return_value = mock_response
        self.assertEqual(fetcher.fetch_price(554), 54321)
        mock_get.assert_called_once_with('http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=554')
