"""class Employee:
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 3
    def HasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print(f"{self.name} Achieved the Target")
        else:
            print(f"{self.name} Not Achieved the Target")
            
employee1 = Employee()
employee1.HasAchievedTarget()
employee2 = 

"""

class Employee:
    NoOfWorkingHours = 12
    
emp1 = Employee()
emp1.name = "Praseesh"

print(f"Employee Name: {emp1.name}, \n Employee WH:{emp1.NoOfWorkingHours}")

Employee.NoOfWorkingHours = 8

print(f"Employee Name: {emp1.name}, \n Employee WH:{emp1.NoOfWorkingHours}")
