# print("Hello World")

# age = 23
# a = None

# print(type(a))

# # case sensitive 
# A = 1
# a ="1"

# if (a==A):
#     print("True")
# else:
#     print(False)

    # typed language ~ implicit
a , b = 1.5 , 3
c = a//b
print(c , type(c)) #output 0.0 ( int to float)
# floor ~ gives closest integer , which is lesser than or equal to float va;ue
# Result of (a//b) is same as floor(a/b)

#single line if statemnt ~ ternary operator
# food = input ("Food : ")
# eat = "Yes" if food=="cake" else "no"
# print(eat)

# num = int(input("Enter any num : "))
# print("Even num") if num/2==0 else print("Odd")

# print("Even num") if num in range(0,1000 ,2) else print("Odd")

#type conversion  & type casting

# type conversion is auto done by python interpreter 
# type casting is manually done 

a = int("2")
b = 2.5
print(a+b , type(a))

#strings

str = "KhushiKaur"

#concatenation
str2 = "concatenation"
# print(str +str2)

# print(len(str2))

#indexing
# print(str[0])

# #slicing

# print(str[:4])
# print(str[0:])
# print(str[:7])
print(str[-4:-2])
str = str.replace("Khushi", "Noor")
print(str.upper())
print(str)

#list --- mutable ( can be easily changed)

marks = [23 , 44 , 56 , 78 , 99]
print(marks)
print(marks[0])
print(len(marks))
marks[0]= 100
marks.append(89)
print(marks)

marks.sort(reverse=True) #printing list in descending order ( sroting in reverse order)
print(marks)
marks.remove(44)
marks.pop(1)
print(marks)

#Tuples --- same as list however( immutable can't be changed )
a = (1,2,3,4,5)
b = ()
c = (1,)
d = (1) # output - type (int)

#methods in tuple
print(a , type(c))
print(a.index(1))
print(a.count(1))

#palindrome ~  121 - 121
l1 = [ 1,2,1]
l2 = [ 1,2,3]

c1= l1.copy() #shallow copy
c1.reverse()

print("Plaindrome") if (c1==l1) else print("Not a palindome")

#Dict -- stores data in key value pairs (mutable) , unordered

info = {
    "name" : "Navv", 
    "age" : 87 ,
}
info["name"] = "Khushi" #previous value overwrite

print(info.get("name"))


#sets ----- unordered items , elements are unique & immutable 

collection = { 1,2,2,2,2,2,6,2,"World"}

print(collection)

s = {}
s1 = set()
s1.add(1)
s1.add(2)

print( s1,type(s1))

#loops ~ repeat instructions


# x = 1 #iterator
# while (x<=5):
#     print(x , "While")  #iteration
#     x+=1


# i = 1
# while(i<=10):
#     print(6*i)
#     i+=1


#functions -- bloack of statements that pefroms a specific task

#function definition
def sum(a,b):  # parameters  

    print(a+b)
    return a + b
    

val = sum(5,6) #function call ; arguments
# print(val)

#recursion -- funcion calling itself 

# def show(n):
#     if (n==0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# file i/o 
#reading mode 

# f = open("demo.txt" , "r")
# data = f.read()
# print(data)
# f.close()

#write mode

f = open("demo.txt" , "w")
data = f.write("I am learning python")
print(data)
f.close()

#deleting a file 

import os
# os.remove("demo.txt")

#OOPS -- obejct oreinted programming

#class & objects

class Info: #class
    # name = "Jyoti Malhotra"
    # age  = 23
    # @staticmethod
    def __init__(self , name):
        self.name = name 
        print(f"Additng new stundent in database \n \t {self.name} ")
        

s1 = Info("Jyoti Malhotra") #instance or object
# s1.name = "Jyoti Malhorta" #instance attribute
# print(s1.name)

# class Car:
#     brand = "ferrari"

# car1 = Car()
# print(car1.brand)

class Get:
    company = "Google"

    def __init__(self , name , age):
        self.name = name 
        self.age = age
        print(f'Candidate {name} , {age}')

    @staticmethod
    def info():
        print(f"Selected in {Get.company}")
    

hired = Get("Jyoti Malhorta" , 23)
hired.info()
#important

# 4 pillars of OOP'S

# Abstraction ----- hiding the implementation details of a class & only 
# showing the essential features to the user
# Hinding unnecesary details 

# Encapsulation --- Wrapping data & function into single unit ( object)

#Inheritance
# Polymorphism

# privte like attributes 
class Account:
    def __init__(self , acc_no , acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #private ( use __ to make attribute private unable to access outside class )

acc1 = Account("12345" , "abcde")
# print(acc1.acc_no)
print(acc1.acc_no)
# print(acc1.acc_pass)


class Person:
    __name = "anynoymous" #private attribute

    def __hello(self): #private method
        print("Hello Person")

p1 = Person()
# print(p1.__name)

# p1.hello()
# Person.hello(p1)

# Inheritance 
# When one class( child class) derives the properties & methods of another class ( base class )

class Car:

    color = "black"
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")

class SwiftCar(Car):
    def __init__(self , name):
        self.name = name
        print(f"Car is {name} & color is {Car.color}")

car1 = SwiftCar("Fortuner")
# car2 = SwiftCar("Prius")

car1.stop()



