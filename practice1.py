weight = input('Weight: ')
unit = input('(L)bs or (K)g : ')

weight = float(weight)

if unit.upper() == 'L':
    weight = weight * 0.45
    print('Your weight in Kg is ' + str(weight))
else :
    weight = weight/0.45
    print('Your weight in pound is ' + str(weight))
