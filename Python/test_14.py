# Python Object Oriented Programming :
# Classes: class is a template / blue-print for real-world entities
# Class in Python: class is a user-defined data-type
# Attributes & Methods : properties & behavior
# Objects : Objects are specific instances of a class
# Creating the first class:
class Phone:
    def make_call(self):
        print("Making a call")
    def play_game(self):
        print("I'm playing a game")

p1 = Phone()
p1.make_call()
p1.play_game()
# Adding Parameter to the Class:
class Phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return(self.color)
    def show_cost(self):
        return(self.cost)
    def make_call(self):
        print("Making a call")
    def play_game(self):
        print("I'm playing a game")
p2 = Phone()
p2.set_color("Pink")
p2.set_cost(10000)
s=p2.show_color()
a = p2.show_cost()
print(s)
print(a)
p2.make_call()
p2.play_game()


