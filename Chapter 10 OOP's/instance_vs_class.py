class Employee :

    language ="py" #This is a class attribute 
    salary = 35000


harry = Employee() #object instantitaion

harry.language ="Python" # This is an instance(object) attribute

print( harry.salary , harry.language)

# instance attribute takes preference over class attributes