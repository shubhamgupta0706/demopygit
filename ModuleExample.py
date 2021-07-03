import utils

number = input('Enter List Values(Separated by space): ')
number = number.split(" ")
print(utils.find_max(number))