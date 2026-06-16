#Free shipping check
def qualifies_for_free_shipping(amount: float, threshold: float) -> bool:
    return amount >= threshold

print(qualifies_for_free_shipping(75.0, 50.0))  # True
print(qualifies_for_free_shipping(40.0, 50.0))  # False
