def prime_numbers(limit):
    total = 0
    for number in range(limit+1):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                total += number
    return total

print(prime_numbers(20))
