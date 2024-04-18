class Table:
    def __init__(self, material, age) :
        self.material = material
        self.age = age

table1 = Table("Wood", 5)
print (table1.age)
a = table1.material
print(a)

table2 = Table("Steel", 5)
print(f"This is my {table1.material} table, and {table1.age} year old")

table1.age = 10
table1.material = "Fe"
print(f"This is my {table1.material} table, and {table1.age} year old")

"""
Here  material, age are instance 
change the value of the instance variable only affect the instance variable 
"""