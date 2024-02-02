# Multi-Level Inheritance :
class Parent():
    def assign_name(self, name):
        self.name = name

    def show_name(self):
        return self.name

class Child(Parent):
    def assign_age(self,age):
        self.age = age

    def show_age(self):
        return self.age

class Grandchild(Child):
    def assign_gender(self,gender):
        self.gender = gender

    def show_gender(self):
        return self.gender

c1 = Grandchild()

c1.assign_name("Kalpana")
c1.assign_age("26")
c1.assign_gender("Female")

s1 = c1.show_name()
print(s1)
s2 = c1.show_age()
print(s2)
s3 = c1.show_gender()
print(s3)