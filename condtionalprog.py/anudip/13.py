

#Q13:


class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class Car(Vehicle):

    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def display(self):
        print(self.brand, self.speed, self.fuel_type)


car = Car("Toyota", 180, "Petrol")
car.display()












