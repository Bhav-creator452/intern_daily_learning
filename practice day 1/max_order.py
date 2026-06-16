#Stretch — biggest order without max()
def largest_order(amounts: list[float]) -> float:
    if not amounts:
        return 0.0

    largest = amounts[0]

    for amount in amounts:
        if amount > largest:
            largest = amount

    return largest

print("Largest order:", largest_order([120, 88.55, 99.55]))