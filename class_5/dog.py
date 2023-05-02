class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        print(f"{self.name} says Guao guao!!")
    
    def info(self):
        print(f"I am {self.name} and I am a {self.age} years old {self.breed}")

dasha = Dog(name="Dasha", breed= "Siberian Husky", age=0.75)
print(dasha.info())
print(dasha.bark())