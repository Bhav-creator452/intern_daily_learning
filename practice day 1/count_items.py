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