#email validation
def is_valid_email(email: str) -> bool:
    if email.count("@")!=1:
        return False
    username, domain = email.split("@")

    if username=="" or domain=="":
        return False
    
    if "." not in domain:
        return False
    
    name, extension = domain.rsplit(".", 1) 

    if name=="" or extension=="":
        return False
    return True

print(is_valid_email("anna@shop.com"))      # True
print(is_valid_email("anna.shop.com"))      # False
print(is_valid_email("@shop.com"))          # False

print(is_valid_email("anna@.com"))         # False
print(is_valid_email("anna@shopcom"))      # False
print(is_valid_email("anna@shop."))        # False
print(is_valid_email("anna@@shop.com"))     # False


#Order Total with Tax
def order_total(price:float,tax_rate:float) -> float:
    tax_amount = price * tax_rate
    total = price + tax_amount
    return total

print(order_total(100.0, 0.01)) 
print(order_total(49.99, 0.0))


#Free shipping check
def qualifies_for_free_shipping(amount: float, threshold: float) -> bool:
    return amount >= threshold

print(qualifies_for_free_shipping(75.0, 50.0))  # True
print(qualifies_for_free_shipping(40.0, 50.0))  # False


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


#average order value
def average_order_value(amounts: list[float]) -> float:
    if not amounts:
        return 0.0
    total = sum(amounts)
    average = total / len(amounts)
    return average

print("Average order value:", average_order_value([100.0, 50.0, 30.0]))  


#count items per category
def count_by_category(items: list[dict]) -> dict:
    counts = {}

    for item in items:
        category = item["category"]

        if category in counts:
            counts[category] += 1
        else:
            counts[category] = 1

    return counts

items=[
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Mouse", "category": "Electronics"},
    {"name": "Notebook", "category": "Stationery"}
]
print("Items by category:", count_by_category(items))


#flag large orders
def flag_large_orders(amounts: list[float], limit: float) -> list[float]:
    flagged = []

    for amount in amounts:
        if amount > limit:
            flagged.append(amount)

    return flagged

print("Large orders:", flag_large_orders([45, 900, 1200, 30],500))  # [900, 1200]


#Stretch — biggest order without max()
def largest_order(amounts: list[float]) -> float:
    if not amounts:
        return 0.0

    largest = amounts[0]

    for amount in amounts:
        if amount > largest:
            largest = amount

    return largest

print("Largest order:", largest_order([120, 880, 45]))  