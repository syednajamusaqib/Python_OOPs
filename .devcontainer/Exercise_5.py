# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
class Vehicle(object):
    color = "White" # Class Variable 
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def print_all(self):
        print(f"Name of Vehicle is {self.name}")
        print(f"Max_speed of Vehicle is {self.max_speed}")
        print(f"Color of Vehicle is {self.color}")
        print(f"Mileage of Vehicle is {self.mileage} \n")

class Bus(Vehicle):
    pass
class Car(Vehicle):
    pass

veh_1 = Bus("silk_line",130,14000)
veh_2 = Car("FMT",140,11000)

veh_1.print_all()
veh_2.print_all()