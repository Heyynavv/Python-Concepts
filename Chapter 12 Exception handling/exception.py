
try :
    a = int(input("Heyy , Enter a number : "))

    print(a)

except ValueError as v:
    print("Heyy enter a number to continue further ")


except Exception as e:
    print(e)

print('Thank you')

# raising a custom error statements 

a = int(input("Enter 1st num :"))
b = int(input("Enter 2nd num :"))

if (b==0):
    raise ZeroDivisionError("Hey our program is not meant to divide num by zero")
else:
    print(f"The divison is {a/b}")

4

