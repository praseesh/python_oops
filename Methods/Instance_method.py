class Vehicle:
    def __init__(self, make, color, gps=False):
        self. make = make
        self.color = color
        self.gps = gps
        
    def info(self):                 #   Getter method
        print(f"Make: {self.make}\nColor: {self.color}\nGPS: {self.gps}")

    def  gps_on(self):         #   Setter method 
        self.gps = True
        print("GPS enabled")
        
car1 = Vehicle("Audi", "Black")
car1.gps_on()
car1.info()
print(car1.gps)