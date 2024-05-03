class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Private attribute
        self.__salary = salary  # Private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

# Create an Employee instance
emp = Employee("John Doe", 50000)

# Access private attribute using getter method
print("Name:", emp.get_name())  # Output: Name: John Doe
print("Salary:", emp.get_salary())  # Output: Salary: 50000

# Modify private attribute using setter method
emp.set_salary(60000)
print("Updated Salary:", emp.get_salary())  # Output: Updated Salary: 60000
