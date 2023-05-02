class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"Start {self.make} {self.model}")
    def stop(self):
        print(f"Stop {self.make}  {self.model}")
    def info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"
    
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def lock_doors(self):
        print(f"Doors of the {self.make} {self.model} are locked")

    
ferrari_458 = Car(make="Ferrari", model="458 Italia", year=2019, num_doors=2)
chevrolet_corvette = Car(make="Chevrolet", model="Corvette", year=2017, num_doors= 2)
ducati_panigale = Vehicle(make="Ducati", model="Panigale", year=2022)

print(ferrari_458.info())
print(chevrolet_corvette.info())
print(ducati_panigale.info())