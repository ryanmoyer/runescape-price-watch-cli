import requests

def fetch_price(item_id):
    item_url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={0}'.format(item_id)
    response = requests.get(item_url)
    item_inner = response.json['item']
    item_price = item_inner['current']['price']
    return str(item_price)
