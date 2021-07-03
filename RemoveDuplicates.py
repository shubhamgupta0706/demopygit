numbers = [10, 65, 8, 9, 7, 8, 10, 65]
for items in numbers:
    if numbers.count(items) > 1:
        numbers.remove(items)
print(numbers)