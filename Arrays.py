from array import *

arr = array('i', [])
n = int(input('Enter the number of elements you want in array: '))

for i in range(n):
    num = int(input('Enter Element: '))
    arr.append(num)

print(arr)

val = int(input('Enter Number to search in array: '))
j = 0
for e in arr:
    if e == val:
        print('Number found at position: ', j)
        break
    j += 1
else:
    print('Number not found.')

