import unittest

import fetcher

class TestFetcher(unittest.TestCase):
    def test_maple_logs(self):
        self.assertEqual(fetcher.fetch_price(1517), 51)
    def test_fire_rune(self):
        self.assertEqual(fetcher.fetch_price(554), 27)
    def test_spirit_shards(self):
        self.assertEqual(fetcher.fetch_price(12183), 24)
