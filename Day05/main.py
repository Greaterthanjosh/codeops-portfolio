from abc import ABC, abstractmethod

# Exercise 1
print("Exercise 1")


class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        print(f"{self.make} {self.model}")

    @abstractmethod
    def wheels(self):
        pass


class Car(Vehicle):
    def wheels(self):
        return 4


class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity

    def describe(self):
        print(f"{self.make} {self.model} - Capacity: {self.capacity} tons")

    def wheels(self):
        return 6


car = Car("Toyota", "Corolla")
truck = Truck("Volvo", "FH16", 20)

car.describe()
truck.describe()


# Exercise 2
print("\nExercise 2")

truck2 = Truck("Mercedes", "Actros", 25)

print(truck2.make)
print(truck2.model)
print(truck2.capacity)


# Exercise 3
print("\nExercise 3")

truck2.describe()


# Exercise 4
print("\nExercise 4")

vehicles = [
    Car("Toyota", "Corolla"),
    Truck("Volvo", "FH16", 20),
    Car("Hyundai", "Elantra"),
    Truck("Mercedes", "Actros", 25)
]

for vehicle in vehicles:
    vehicle.describe()


# Exercise 5
print("\nExercise 5")

for vehicle in vehicles:
    print(f"{vehicle.make} {vehicle.model} has {vehicle.wheels()} wheels.")