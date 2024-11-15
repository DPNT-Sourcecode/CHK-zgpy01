

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

    total = 0


