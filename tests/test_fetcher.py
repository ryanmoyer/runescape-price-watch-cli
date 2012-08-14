import unittest

import fetcher

class TestFetcher(unittest.TestCase):
    def test_item_4721(self):
        self.assertEqual(fetcher.fetch_price(4721), 4721)
    def test_item_4722(self):
        self.assertEqual(fetcher.fetch_price(4722), 4722)
