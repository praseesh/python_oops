class Employee:
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