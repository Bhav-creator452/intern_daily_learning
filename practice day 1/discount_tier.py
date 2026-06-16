#discount tier
def discount_percent(amount: float) -> int:
    if amount >=100:
        return 10
    elif amount >=50:
        return 5
    else:
        return 0
    
print("Discount percent for $120:", discount_percent(120.0))  # 10
print("Discount percent for $60:", discount_percent(60.0))   # 5
print("Discount percent for $30:", discount_percent(30.0))   # 0