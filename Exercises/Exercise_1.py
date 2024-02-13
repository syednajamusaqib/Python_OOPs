# OOP Exercise 1: Create a Class with instances and attributes
class Vehicle(object):
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
# Creating Object for Vehicle Class    
car = Vehicle(67,13000)
print(f"Mileage of your car is {car.mileage}")
