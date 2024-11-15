

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
    }

    offers = {
        'A': (3, 130),
        'B': (2, 45),
    }

    if not isinstance(skus, str):
        return -1

    counts = {}

    for sku in skus:
        if sku in prices:
            counts[sku] = counts.get(sku, 0) + 1

    total = 0
    for sku, count in counts.items():
        if sku in offers:
            offer_count, offer_price = offers[sku]



