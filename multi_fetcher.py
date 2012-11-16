## Take a list of item id and return a string with the item name: price on new lines

import fetcher

def fetch_prices(item_ids):
    lines = []
    for item_id in item_ids:
        name, price = fetcher.fetch_price(item_id)
        lines.append('{0}: {1}'.format(name, price))
    return '\n'.join(lines)
