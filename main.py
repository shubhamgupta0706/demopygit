name = input('Enter Name: ')
len_name = len(name)
if len_name < 3:
    print('Name must be at lease 3 characters long')
elif len_name > 50  :
    print('Name can be maximum 50 characters long')
else :
    print('Name looks good!')