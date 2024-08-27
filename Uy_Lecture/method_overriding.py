class Employee:
    def set_number_of_working_hours(self):
        self.numberOfWorkingHours = 40
    def display_number_of_working_hours(self):
        print(f"Number of Working Hours: {self.numberOfWorkingHours}")
        
class Trainee(Employee):
    def set_number_of_working_hours(self):
        self.numberOfWorkingHours = 50
    def reset_no_of_working_hours(self):
        super().set_number_of_working_hours()
        
employee = Employee()
employee.set_number_of_working_hours()
employee.display_number_of_working_hours()

trainee = Trainee()
trainee.set_number_of_working_hours()
trainee.display_number_of_working_hours()
trainee.reset_no_of_working_hours()
trainee.display_number_of_working_hours()


