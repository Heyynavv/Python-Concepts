# 2005 ~ numpy 
# make calculation fast & quick 
# numpy stands for numerical Python. It provides a high-performance multidimensional array object, and tools for working with these arrays.
# features --- speed , less memeory usage, readable syntax , easy math 

# operations
import numpy as np

temperatures = np.array([10, 15, 20, 25, 30])
avg = np.mean(temperatures)
print(avg)  # output: 20.0

python_list = [10, 15, 20, 25, 30]
print((python_list))  # output: 20.0

numpy_array = np.array([1, 2, 3, 4, 5]) #1D ARRAY
print(numpy_array)  # output: [1 2 3 4 5]

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) #2D ARRAY
print(arr_2d)  # output: [[1 2 3] [4 5 6] [7 8 9]]

#multidimensional array
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) #3D ARRAY
print(arr_3d)  # output: [[[ 1  2  3]
                  #         [ 4  5  6]]
                  #        [[ 7  8  9]
                  #         [10 11 12]]]

default_array = np.zeros((3, 3)) # create a 3x3 array filled with zeros
print(default_array)  # output: [[0. 0. 0.]

ones = np.ones((3, 3)) # create a 3x3 array filled with ones
print(ones)  # output: [[1. 1. 1.]

filled_array = np.full((3, 3), 7) # create a 3x3 array filled with 7
print(filled_array)  # output: [[7 7 7]

arr = np.arange(1, 11) # create a 1D array from 1 to 10 sequence pf numbers 
print(arr)  # output: [ 1  2  3  4  5  6  7  8  9 10]

arr = np.identity(3) # create a 3x3 identity matrix
print(arr)  # output: [[1. 0. 0.]


# properties // calculations

# shape , size , type 

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d.shape) 
print(arr_2d.size) # output: (2, 3)
print(arr_2d.ndim)
print(arr_2d.dtype)

# changing datatype 
arr = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(arr.dtype) # output: float64  

# aggregation function 
arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr)) # output: 15
print(np.mean(arr)) # output: 3.0
print(np.median(arr)) # output: 3.0
print(np.std(arr)) # output: 1.4142135623730951
print(np.min(arr)) # output: 1
print(np.max(arr)) # output: 5


# indexing & slicing
arr = np.array([1, 2, 3, 4, 5])
print(arr[0]) # output: 1 #indexing
print(arr[2:]) # output: [3 4 5] #slicing
print(arr[:3]) # output: [1 2 3]
print(arr[::-1]) # output: [5 4 3 2 1]

# fancy indexing
arr = np.array([1, 2, 3, 4, 5])
print(arr[[0, 2, 4]]) # output: [1 3 5]

# boolean idexing 
arr = np.array([1, 2, 3, 4, 5])
print(arr[arr > 3]) # output: [4 5]



# flattening & ravel & reshaping
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

#faltten
print(arr_2d.flatten()) # output: [1 2 3 4 5 6] #returns a copy  of array in 1D
#ravel
print(arr_2d.ravel()) # output: [1 2 3 4 5 6] #returns a view of array in 1D

print(arr_2d.reshape(3, 2)) # output: [[1 2] #creates 2d into 3d array
                  #         [3 4]
                  #         [5 6]]

#array add , remove , split & more 
arr = np.array([1, 2, 3, 4, 5])
print(np.append(arr, 6)) # output: [1 2 3 4 5 6]
print(np.delete(arr, 2)) # output: [1 2 4 5]
print(np.split(arr, 2)) # output: ([1, 2], [3, 4, 5])

# sorting
arr = np.array([3, 1, 2, 5, 4])
print(np.sort(arr)) # output: [1 2 3 4 5]
