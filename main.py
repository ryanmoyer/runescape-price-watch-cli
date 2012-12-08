# Runescape Price Fetcher
# Author: Ryan Moyer

from __future__ import print_function

from multi_fetcher import fetch_prices

import argparse

parser = argparse.ArgumentParser(description='Grabs item ID.')
parser.add_argument('item_ids', metavar='ITEM_ID', type=int, nargs='+', help='the id for an item')
args = parser.parse_args()

print(fetch_prices(args.item_ids))
