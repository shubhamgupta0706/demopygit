def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['index'] = i
            return True
    else:
        return False


list = [5, 8, 4, 6, 9, 2]

n = 6
index = -1

if search(list, n):
    print("Number found at position: ", index)
else:
    print("Number not found!")



