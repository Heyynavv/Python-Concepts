# printing patterns using recursion 

# def pattern(n):
#     if (n==0):
#         return
#     print("*" * n)
#     pattern(n-1)

# pattern(5)
# print("")

# def pattern(n):
#     if (n==6):
#         return
#     print("*" * n)
#     pattern(n+1)

# pattern(1)

# printing pattern in simplest way using for loop

for i in range(1,6):
    # print("*" * i)
    pass
print("")

for i in range(5,0,-1):
    # print("*" * i)
    pass

for i in range(4):
    pass
    # print(" # " , end="")
# print("")

for i in range(4):
    for i in range(4):
        print(" # " , end="")
    print("")

for i in range(6):
    for j in range(i):
        print("# " , end ="")
    print()

rows = 5

for i in range(1, rows + 1):
    spaces = ' ' * (rows - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

for i in range(1, 6):
    print(' ' * (5 - i) + '*' * (2 * i - 1))