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

    def test_three_items(self, mock_fetch_price):
        item_ids = [554, 12345, 54321]
        expected = '''fire rune: 15
pickle: 14321
frost dragon bones: 123k'''

        # Provide different return values for fetch_price() every time.
        fetch_price_retvals = {
            54321: ('frost dragon bones', '123k'),
            12345: ('pickle', '14321'),
            554: ('fire rune', '15')}
        def fetch_price_side_effect(item_id):
            return fetch_price_retvals[item_id]
        mock_fetch_price.side_effect = fetch_price_side_effect

        self.assertEqual(multi_fetcher.fetch_prices(item_ids), expected)
        
