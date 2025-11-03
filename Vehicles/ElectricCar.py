from .Car import Car

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self.battery_level = 100
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model} (Electric)"
    
    def charge_battery(self, amount):
        self.battery_level = min(100, self.battery_level + amount)