def div(a, b):
    return a / b


def smart_div(fun):
    def inner(a, b):
        if a < b:
            a,b = b,a
        return fun(a, b)
    return inner


div = smart_div(div)

print(div(2, 4))