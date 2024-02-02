# Creating a Class with Constructor:
class Employee:
    def __init__(self,company,name,age,salary,gender):
        self.company=company
        self.name= name
        self.age=age
        self.salary=salary
        self.gender=gender

    def show_employee_details(self):
            print("I a Employee of",self.company)
            print("Name of the employee is",self.name)
            print("Age of a employee is",self.age)
            print("Salary of employee is",self.salary)
            print("Gender of employee is", self.gender)

e1 = Employee('TCS','Jan',22,700000,'Female')
e1.show_employee_details()

