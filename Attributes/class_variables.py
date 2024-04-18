class Table:
    legs = 4
    def __init__(self, material, age) :
        self.material = material
        self.age = age
        
table1 = Table("Wood", 5)
Table.legs = 6

print(table1.legs)

"""
Table.legs = 6
This is the correct method of changing the values of class attributes

"""