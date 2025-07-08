from datetime import date 
# a = 12
# b = 34
# c= 45
# average = (a+b+c)/3
# print(average)

#Function Definiton
# def avg():
#     a = int(input("Enter number: "))
#     b = int(input("Enter number: "))
#     c = int(input("Enter number: "))
#     average = (a+b+c)/3
#     print(average)

# avg() #Function Call
# print("Thank you ")
# avg()

# def todays_date():
   
#     x=date.today()
#     print(x)
    
# todays_date()

#functions with arguments

def goodDay(name):
    print("Good Day" , name)

goodDay("Navv")

# default arguments
def goodDay(name , ending="Thank you"):
    print(f"Good Day {name}")
    print("\t" , ending)

goodDay("Navv")