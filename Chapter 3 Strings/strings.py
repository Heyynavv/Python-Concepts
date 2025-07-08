name = "Navneet"

# strings are mutable 

# slicing in strings 

short_name = name[0:3]
print(short_name)

# negative slicing

print(name[-4: -1])
print(name[1: 4])
print(name[:7]) # same as [0:7]
print(name[3:]) # same as 3:length of string

# skip slicing

a = "1234567890"
print(a[0:5])
print(a[0:5:2])  # first resolve 0:5 , then pick 1st & keep skipping 2 iterations

#reversing a string

abc = " HEYYY \n \'This is reversing string in a simple way\'"
print(abc[::-1])