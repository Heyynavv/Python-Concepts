class Employee: #base class / parent class

    company ="ITC"

    def __init__(self):
        print("Constructor of Employee")

    def show(self):
        # print(f"The name is {self.name} and the salary is {self.salary}")
        print("This is show method")

class Coder(Employee):

    

    def __init__(self):
        # super().__init__()
        print("Constructor of Coder")
        
    def getinfo(self):
        print("This is get info method")


class Programmer(Coder): #inherited / child class 
    def __init__(self):

        super().__init__() # also runs construtor of parent class
        print("Constructor of Programmer")
    

    company = "ITC Infotech "


# a = Employee()
# b = Coder()
c = Programmer()

# c.show()
# c.getinfo()
