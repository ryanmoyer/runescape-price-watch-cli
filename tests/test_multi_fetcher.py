import unittest

from mock import patch

import multi_fetcher

@patch('fetcher.fetch_price')
class TestMultiFetcher(unittest.TestCase):
    def test_no_items(self, mock_fetch_price):
        self.assertEqual(multi_fetcher.fetch_prices([]), '')

    def test_one_item_fire_rune(self, mock_fetch_price):
        item_ids = [554]
        expected = 'fire rune: 15'
        mock_fetch_price.return_value = ('fire rune', '15')
        self.assertEqual(multi_fetcher.fetch_prices(item_ids), expected)
        mock_fetch_price.assert_called_once_with(554)
