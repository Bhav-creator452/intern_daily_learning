'''dataclasses lets you create classes that are primarily used to store data with less boilerplate code. It automatically generates special methods like __init__(), __repr__(), and __eq__() based on the class attributes.'''

#creating a class without dataclass

class Customer:
    def __init__(self, id, email, country, total_past_orders=0):
        self.id = id
        self.email = email
        self.country = country
        self.total_past_orders = total_past_orders

customer1 = Customer("123", "john@example.com", "USA")
customer2 = Customer("456", "jane@example.com", "Canada")
print(customer1)
print(customer1.email)
print(customer2)
print(customer2.email)

#creating a class with dataclass
from dataclasses import dataclass
@dataclass
class Customer:
    id: str
    email: str
    country: str
    total_past_orders: int = 0
customer1 = Customer("123", "john@example.com", "USA")
customer2 = Customer("456", "jane@example.com", "Canada")
print(customer1)
print(customer1.email)
print(customer2)
print(customer2.email)
