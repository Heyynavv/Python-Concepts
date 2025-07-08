
class Students :
    marks = 80
    age = 23

    def __init__(self , name ,marks , age): #dunder method which is atuomatically called & starts with double underscore
        self.name = name
        self.age = age
        self.marks = marks
        print("i am creating an object")

    def getinfo(self):
        print(f"The marks is {self.marks} , & the age is {self.age}")

    @staticmethod #used when we don;t want to define self parameter to run the functions inside a class using object
    def greet():
        print("Good Morning")

nav = Students("Khushi" , 100 , 23)  

# nav.name="Noor"

print(nav.name , "\t ", nav.marks , nav.age)

# nav.getinfo()
# nav.greet()