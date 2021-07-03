a = 5
b = 2
try:
    print("Resource Open.")
    print(a/b)
    k=int(input("Enter number: "))
except ZeroDivisionError as e:
    print("Hey, we cannot divide a number by zero: ", e)

except ValueError as e:
    print("Entered is not a valid number: ", e)

finally:
    print("Resource Closed.")