class Sum:
    # def __init__(self,a,b) :
    #     self.a = a
    #     self.b = b
        
    def input_num(self):
           self.a = int(input("Enter First number"))
           self.b = int(input("Enter Second number"))
           
    def sum (self):
        self.sum = self.a + self.b
        
    def display(self):
        print(f"Sum is : {self.sum}")
        
s = Sum()
s.input_num()
s.sum()
s.display()