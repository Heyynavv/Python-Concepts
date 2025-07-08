class Employee: #base class / parent class

    company ="ITC"

    def show(self):
        # print(f"The name is {self.name} and the salary is {self.salary}")
        print("Child/Inherited class object can easily access base/parent class methods")

class Coder():
    def getinfo(self):
        print("This is second base class ")


class Programmer(Employee , Coder): #inherited / child class 
    def __init__(self):
        print("Understanding Multiple inheritance")
    company = "ITC Infotech "


a = Employee()
b = Coder()
c = Programmer()

c.show()
c.getinfo()