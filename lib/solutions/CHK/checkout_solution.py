

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
    }

    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
    }

    free_offers = {
        'E': ('B', 2),
        'F': ('F', 2),
    }

    if not isinstance(skus, str) or not all(char in prices for char in skus):
        return -1

    counts = {}

    for sku in skus:
        counts[sku] = counts.get(sku, 0) + 1

    for free_sku, (required_sku, required_count) in free_offers.items():
        if free_sku != required_sku:
            if free_sku in counts:
                free_items = counts[free_sku] // required_count
                counts[required_sku] = counts.get(required_sku, 0)
                counts[required_sku] = max(0, counts[required_sku] - free_items)

    for free_sku, (required_sku, required_count) in free_offers.items():
        if free_sku == required_sku:
            counts[free_sku] -= counts[free_sku] // (required_count + 1)

    total = 0

    for sku, count in counts.items():
        if sku in offers:
            for offer_count, offer_price in offers[sku]:
                total += (count // offer_count) * offer_price
                count = count % offer_count
            total += count * prices[sku]
        else:
            total += count * prices[sku]
    return total





