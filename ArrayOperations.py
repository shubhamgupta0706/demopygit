from numpy import *

arr = array([1, 2, 4, 6, 7])
arr1 = arr + 5
'''print('Array: ', arr)
print('Sin of array: ', sin(arr))
print('Cos of array: ', cos(arr))
print('Log of array: ', log(arr))
print('Square root of array: ', sqrt(arr))
print('Sum of array: ', sum(arr))
print('Min of array: ', min(arr))
print('Max of array: ', max(arr))
print('sort of array: ', sort(arr))

print(concatenate([arr, arr1]))'''

# Copying the array
arr2 = array([4, 5, 8, 9])
# arr3 = arr2  # will have same address - Also called shallow copy
# arr3 = arr2.view()  # will have different address - Also called shallow copy
arr3 = arr2.copy()   # will have different address - Also called deep copy
arr3[1] += 1
print(arr2)
print(arr3)
print(id(arr2))
print(id(arr3))