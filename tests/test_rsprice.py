import unittest

from rsprice import to_float


class TestToFloat(unittest.TestCase):
    def test_normal_int(self):
        self.assertEqual(to_float('456'), 456)

    def test_normal_real(self):
        self.assertEqual(to_float('12.456'), 12.456)

    def test_thousand_int(self):
        self.assertEqual(to_float('456k'), 456e3)

    def test_thousand_real(self):
        self.assertEqual(to_float('12.456k'), 12.456e3)

    def test_million_int(self):
        self.assertEqual(to_float('943m'), 943e6)

    def test_million_real(self):
        self.assertEqual(to_float('811.34m'), 811.34e6)

    def test_billion_int(self):
        self.assertEqual(to_float('943b'), 943e9)

    def test_billion_real(self):
        self.assertEqual(to_float('811.34b'), 811.34e9)
