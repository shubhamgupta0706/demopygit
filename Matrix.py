from numpy import *

arr = array([
    [1, 2, 3, 8, 67, 12],
    [4, 5, 6, 43, 36, 21],
])

arr2 = arr.flatten()  # multi dimension to 1 dimensional
arr3 = arr2.reshape(2, 2, 3)

# print(arr)
# print(arr2)
# print(arr3)

# m = matrix(arr)
# print(m)
m1 = matrix('1, 2, 3;  4, 5, 6;  7, 8, 9')
print(m1)
print(diagonal(m1))