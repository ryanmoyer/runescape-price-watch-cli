# Runescape Price Fetcher
# Author: Ryan Moyer

from __future__ import print_function
import argparse
import requests

parser = argparse.ArgumentParser(description='Grabs item ID.')
parser.add_argument('item_id', metavar='ITEM_ID', type=int, help='the id for an item')
args = parser.parse_args()
item_id = args.item_id
item_url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={0}'.format(item_id)
request = requests.get(item_url)
item_price = request.json['item']['current']['price']
print(item_price)
