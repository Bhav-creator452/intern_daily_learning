#class - blueprint for creating objects
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person("John",36)
print(p1.name,p1.age)


class employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self,fname,lname,pay):  
        self.fname = fname   #instance variables -> variables that are unique to each instance
        self.lname = lname
        self.pay = pay
        self.email = fname + "." + lname + "@company.com"
        employee.num_of_emps += 1
emp1 = employee("John","Doe",50000)
emp2 = employee("Jane","Smith",60000)
print(employee.num_of_emps)
# print(emp1.fname)
# print(emp1.lname)
# print(emp1.pay)
# print(emp1.email)

def fullname(self):
    return '{} {}'.format(self.fname,self.lname)
employee.fullname = fullname
print(employee.fullname(emp1))
print(emp1.fullname())
print(emp1.email)

def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)
employee.apply_raise = apply_raise
emp1.apply_raise()
print(emp1.pay)

class car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
        
car1 = car("red", 10000)
car2 = car("blue", 20000)

print(f"{car1.color} car has {car1.mileage} miles")
print(f"{car2.color} car has {car2.mileage} miles")