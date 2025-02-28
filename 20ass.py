class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles

    def describe_vehicle(self):
        print(f"This {self.year} {self.make} {self.model} has {self.mileage} miles.")

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_vehicle(self):
        print(f"This {self.year} {self.make} {self.model} has {self.mileage} miles and a {self.battery_size} kWh battery.")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size

    def describe_vehicle(self):
        print(f"This {self.year} {self.make} {self.model} has {self.mileage} miles and a {self.engine_size} cc engine.")

my_tesla = ElectricVehicle('Tesla', 'Model S', 2021, 75)
my_tesla.drive(100)
my_tesla.describe_vehicle()

my_harley = Motorcycle('Harley-Davidson', 'Softail', 2023, 1800)
my_harley.drive(50)
my_harley.describe_vehicle()