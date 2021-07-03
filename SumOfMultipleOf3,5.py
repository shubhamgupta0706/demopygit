def mul_sum(limit):
    total = 0
    for number in range(3, limit):
        if number % 3 == 0 or number % 5 == 0:
            total += number
            print(number, end=" ")
    return total

print(f"Sum of the mentioned numbers is = {mul_sum(21)}")