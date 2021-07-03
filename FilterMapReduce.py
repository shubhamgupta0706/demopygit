from functools import reduce

nums = [2, 6, 8, 7, 9, 13, 39, 41, 24, 65]

evens = list(filter(lambda n: n % 2 == 0, nums))
doubles = list(map(lambda n: n*2, evens))
total = reduce(lambda a, b: a+b, doubles)
print(evens)
print(doubles)
print(total)

