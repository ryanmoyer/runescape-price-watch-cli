# Runescape Price Fetcher
# Author: Ryan Moyer

from __future__ import print_function
import fetcher
import argparse

parser = argparse.ArgumentParser(description='Grabs item ID.')
parser.add_argument('item_id', metavar='ITEM_ID', type=int, help='the id for an item')
args = parser.parse_args()
item_id = args.item_id

print(fetcher.fetch_price(item_id))
