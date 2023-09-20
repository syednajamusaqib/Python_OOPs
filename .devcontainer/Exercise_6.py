"""Create a Bus child class that inherits from the
 Vehicle class. The default fare charge of any 
 vehicle is seating capacity * 100. If Vehicle is 
 Bus instance, we need to add an extra 10% on full 
 fare as a maintenance charge. So total fare for 
 bus instance will become the final amount = total 
 fare + 10% of the total fare."""
class Vehicle(object):
    def __init__(self,name,max_speed,capacity):
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def total_amount(self):
        return (self.fare()+(self.fare()/10))

bus = Bus("Silk_line",130,50)
print(f"Your final amount is {bus.total_amount()}")
        