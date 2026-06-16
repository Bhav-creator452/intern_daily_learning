#average order value
def average_order_value(amounts: list[float]) -> float:
    if not amounts:
        return 0.0
    total = sum(amounts)
    average = total / len(amounts)
    return average

print("Average order value:", average_order_value([100.0, 50.0, 30.0]))  