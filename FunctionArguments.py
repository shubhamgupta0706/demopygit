def person(name, age=18):  # Default Argument
    print(name)
    print(age)


def sum(a, *b):  # Variable length Argument
    c = a
    for i in b:
        c += i
    print(c)


# person('Shubham', 23)
sum(5, 6, 9, 6, 24)