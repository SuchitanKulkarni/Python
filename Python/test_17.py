# Over-riding init Method:
class Vehicle :
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost

    def show_Vehicle_detils(self):
        print("Mileage of the vehicle is",self.mileage)
        print("Cost of the vehicle is",self.cost)
        print("I am a vehicle")

c1 = Vehicle(600,1000000)
c1.show_Vehicle_detils()
class Car(Vehicle) :
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres = tyres
        self.hp = hp
    def show_Car_details(self):
        print("Numbers of tyres are",self.tyres)
        print("Horse power of a Car is",self.hp)
        print("I am a Car")
c1 = Car(500,100000098,6,799)
c1.show_Car_details()
c1.show_Vehicle_detils()