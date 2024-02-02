# Types of Inheritance :
# Multiple Inheritance : In multiple inherits from more than 1 parent class
class parent1() :
    def assign_string_one(self,str1):
        self.str1 = str1

    def show_string_one(self):
        return self.str1
class parent2():
    def assign_string_two(self,str2):
        self.str2 = str2

    def show_string_two(self):
        return self.str2
class Derived(parent1,parent2) :
    def assign_string_three(self,str3):
        self.str3 = str3

    def show_string_three(self):
        return self.str3
c1 = Derived()
c1.assign_string_one("I am from parent1")
c1.assign_string_two("I am from parent2")
c1.assign_string_three("I am from Derived")
s1 = c1.show_string_one()
print(s1)
s2 = c1.show_string_two()
print(s2)
s3 = c1.show_string_three()
print(s3)

