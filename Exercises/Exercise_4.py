class Vehicle(object):
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def seating_capacity(self,capacity):
        return f"The seating capacity of a {self.name} is {capacity}"


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
    
my_bus = Bus("FMT",140,11000)
print(my_bus.seating_capacity())