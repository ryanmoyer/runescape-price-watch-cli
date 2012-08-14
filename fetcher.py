import requests

def fetch_price(item_id):
    item_url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={0}'.format(item_id)
    request = requests.get(item_url)
    item_inner = request.json['item']
    item_price = item_inner['current']['price']
    return item_price
