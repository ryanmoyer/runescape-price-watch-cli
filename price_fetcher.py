# Runescape Price Fetcher
# Author: Ryan Moyer

from __future__ import print_function
import argparse

parser = argparse.ArgumentParser(description='Grabs item ID.')
parser.add_argument('item_id', metavar='ITEM_ID', type=int, help='the id for an item')
args = parser.parse_args()
print(args.item_id)
