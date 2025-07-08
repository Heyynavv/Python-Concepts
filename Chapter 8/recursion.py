# factorial(n) = n* factorial(n-1)
# function calling itself is recursion 
def fact(n):
    if (n==1 or n==0):
        return 1 
    return n * fact(n-1)

n = int(input('Enter any number: '))
print(f"The factorial of this number is : {fact(n)}")

# printing patterns using recursion 

def pattern(n):
    if (n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(5)

print("")

def pattern(n):
    if (n==6):
        return
    print("*" * n)
    pattern(n+1)

pattern(1)