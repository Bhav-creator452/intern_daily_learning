#Order Total with Tax
# add validation
# negative values
# and 0 checks
def order_total(price:float,tax_rate:float) -> float:
    tax_amount = price * tax_rate
    total = price + tax_amount
    return total

print(order_total(100.0, 0.01)) 
print(order_total(49.99, 0.0))
print(order_total(-100.0, 0.01)) 
print(order_total(100.0, -0.01)) 