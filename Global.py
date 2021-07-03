a = 10
b = 20


def something():
    global a
    a = 15
    print('Global a: ', a)
    x = globals()['b']
    print('Global b: ', x, b)
    print(id(x), id(b))

something()