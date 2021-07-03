def toTen():
    for i in range(1, 11):
        yield i**2


values = toTen()
print(values.__next__())
for i in values:
    print(i)
