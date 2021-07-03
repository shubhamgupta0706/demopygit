from numpy import *
# arr = array([1, 5, 7, 9, 34, 4.0])
# arr = array([1, 5, 7, 9, 34, 4.0], int)
arr = linspace(0, 15, 16)  # will divide the numbers into 16 different parts
arr1 = arange(1, 15, 2)   # will give the numbers from 1-15 with step 2
arr2 = logspace(1, 40, 5) # will divide the log values into five parts
arr3 = zeros(5, int)
arr4 = ones(6)
# print(arr2.dtype)
# print(arr2)
print('%.2f' %arr2[4])
print(arr3)
print(arr4)