
# self is a instance of a class , it automatically passsed with a function call from an object

class Employee :

    language ="py" #This is a class attribute 
    salary = 35000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod #used when we don;t want to define self parameter to run the functions inside a class using object
    def greet():
        print("Good Evening")

harry = Employee("python " , "Navv") #object instantitaion

harry.language ="Python" # This is an instance(object) attribute

print( harry.salary , harry.language)
# harry.getinfo()
Employee.getinfo(harry) #calling flow // classname ~ functionname ~ objectname

class Students :
    marks = 80
    age = 23

    def getinfo(self):
        print(f"The marks is {self.marks} , & the age is {self.age}")

    @staticmethod #used when we don;t want to define self parameter to run the functions inside a class using object
    def greet():
        print("Good Morning")

nav = Students() 
nav.name="Noor"

print(nav.name , "\n" ,  "\t ", nav.marks , nav.age)

nav.getinfo()
nav.greet()
# Students.getinfo(nav)














