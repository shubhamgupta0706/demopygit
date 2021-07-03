index = -1


def binSearch(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l+u) // 2
        if list[mid] == n:
            globals()['index'] = mid
            return True
        else:
            if n > list[mid]:
                l = mid+1
            else:
                u = mid-1


list_1 = [5, 8, 4, 6, 9, 2]
list_1.sort()

n=4
print(list_1)
if binSearch(list_1, n):
    print("Number found at position: ", index)
else:
    print("Number not found!...")