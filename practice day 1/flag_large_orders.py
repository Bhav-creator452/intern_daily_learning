#flag large orders
def flag_large_orders(amounts: list[float], limit: float) -> list[float]:
    flagged = []

    for amount in amounts:
        if amount > limit:
            flagged.append(amount)

    return flagged

print("Large orders:", flag_large_orders([45, 900, 1200, 30],500))  # [900, 1200]