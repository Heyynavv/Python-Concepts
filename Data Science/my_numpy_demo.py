# ------------------------------------ DATA SCIENCE - MASTERING THE ESSENTIALS-----------------
# source - certification course from Scaler 

# Vectors & Matrices 
# Vector - 1D list or list of numbers
# Matrices - 2D list or list of list of numbers , list of vectors 

import numpy as np

python_list = [1,2,3,4,5,]

# creating a numpy array 
numpy_arr = np.array(python_list)
print(len(numpy_arr))

l2 = [[1,2] , [3,4]]
np_array2 = np.array(l2)

print(np_array2) # 2d list
print(np_array2.shape)

# range function in list & numpy 
print(list(range(6)))
print(np.arange(6))

# to get a random value 
x= np.random.randint(1,100)
print(x)

#transpose & broadcasting

#transpose - swaps rows with columns & columns with rows

marks = [[1,2,3] , [4,5,6] , [7,8,9]]
marks_arr = np.array(marks)
print(marks_arr)
print()
transpose = marks_arr.T
print(transpose)

#Broadcasting - allows to add matrices of different shapes

matric = np.array([[1,2], [3,4] , [5,6]])
print(matric)
print(matric.shape)

#using reshaping on 1D vector

vector = np.array([1,2,3])
print(vector.shape , matric.shape)
broadcasted = matric + vector.reshape(3,1) # reshaped the vector instead of transpose & tranpose will not work on 1D vector
print(broadcasted)

# using .T on 2D vector

vector = np.array([[1,2,3]])
print(vector.shape , matric.shape)
broadcasted = matric + vector.T 
print(broadcasted)


#matrix multiplication

matrix1 = np.array([[1,2] , [4,5]])
matrix2 = np.array([[10,20], [40,50]])

x = matrix1 @ matrix2 #using @
y = np.dot(matrix1 , matrix2) #using np.dot()
z = np.matmul(matrix1 , matrix2) #using np.matmul()
print(x , y)

print()
print(z)

#tensors - kinda 3D array

tensor3D = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(tensor3D.shape)  # (2, 2, 2)

