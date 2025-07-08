# way to acess a method form a class   

class Employee :
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute a is {cls.a}") #self denotes instance attribute

e = Employee()
e.a=45
e.show()
# print(e.a)