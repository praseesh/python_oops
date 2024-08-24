class Employee:
    def __init__(self, name):
        self.name = name
        
    def printing_emp_name(self):
        print(f"The Employee Name id {self.name}")
        
employee1 = Employee("Jacob")
emp2 = Employee("David")
print(emp2.name)
emp2.printing_emp_name() 