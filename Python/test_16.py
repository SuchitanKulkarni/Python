# Inheritance of Python: with inheritance one class can derive the properties of another class
class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_vehicle_details(self):
        print("I am a Vehicle")
        print("Mileage of the vehicle is",self.mileage)
        print("Cost of the vehicle is", self.cost)
v1 = Vehicle(300,60000)
v1.show_vehicle_details()

class Car(Vehicle):
    def show_car(self):
        print("I am a Car")

c1 = Car(400,80000)
c1.show_vehicle_details()
c1.show_car()

