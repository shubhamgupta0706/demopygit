tests = int(input())

for i in range(tests):
    string = ''
    n, m = list(map(int, input().split()))
    maximum = 0
    for row in range(n):
        string = input()
        if len(string) == m:
            count = string.count('#')
            if count > maximum:
                maximum = count
    print(maximum)





