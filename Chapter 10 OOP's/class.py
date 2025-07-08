# class is a blue print to create an object

# Object is kinda instantiation of a class , when a class is defined , a template is defined. Memory is allocated
# # only after object instantiation

class Employee :

    language ="py" #This is a class attribute 
    salary = 35000


harry = Employee() #object instantitaion
harry.name = "Haerry" #object attribute

print( harry.name , harry.salary , harry.language)

rohan = Employee()
rohan.name = "Rohann roo roo" #instance (object) attribute
print(rohan.name , rohan.salary , rohan.language)

# here name is object attribute while salary & languagae are class attribute as they directly 
# belongs to the class
