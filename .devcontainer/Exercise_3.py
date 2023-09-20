# OOP exercise 3: Create a child class of Vehicle
class Vehicle(object):
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

# Creating Object for class
Silk_line = Bus("silk_line Express",130,14000)
print(f"Max_speed of your bus is {Silk_line.max_speed}")