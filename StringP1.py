tests = int(input())
vowels = ('a', 'e', 'i', 'o', 'u')
for i in range(tests):
    lower = 0
    upper = 0
    string = input()
    for j in vowels:
        if j in string:
            lower += 1
        if j.upper() in string:
            upper += 1
    if lower == 5 or upper == 5:
        print('lovely string')
    else:
        print('ugly string')


