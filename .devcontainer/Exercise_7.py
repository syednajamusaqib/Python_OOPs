# To which class object belongs to
class Vehicle(object):
    def __init__(self,name,max_speed,capacity):
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity

class Bus(Vehicle):
    pass

bus = Bus("Silk_line",130,50)
print(type(bus))