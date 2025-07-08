# Inheritanc is a way of creating a new class from existing class 

class Employee: #base class / parent class

    company ="ITC"

    def show(self):
        # print(f"The name is {self.name} and the salary is {self.salary}")
        print("Child/Inherited class object can easily access base/parent class methods")


class Programmer(Employee): #inherited / child class 
    company = "ITC Infotech "
    def showLanguage(self):
        # print(f"The name is {self.name} and the salary is {self.language}")
        print("Base class object can't access child class methods")


a = Employee()
b = Programmer() 
# b.name = "Khushiiiii"
# b.salary = 1000
print(a.company , b.company)
print(b.show()) #Accessing this function from another class object
# print(a.showLanguage()) # Base class object can't access child class methods



