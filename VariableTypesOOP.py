class Car:
    wheel = 4  # Class Variables / Static Variables
    doors = 4

    def __init__(self, mil, com):
        self.mil = mil  # Instance Variables
        self.com = com


car1 = Car(10, 'BMW')
car2 = Car(15, 'Honda')

Car.wheel = 6

print(car1.mil, car1.com, car1.wheel, car1.doors)
print(car2.mil, car2.com, car2.wheel, car2.doors)
