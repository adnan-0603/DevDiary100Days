"""
Factorial Finder: Create a function to find the factorial of a number
-solved by Adnan
"""


def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# Taking input from the user

try:
    number = int(input("Enter a non negative Integer: "))
    if number < 0:
        print("please enter a non-negative integer.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is  {result}")
except ValueError:
    print("Invalid input! please enter an integer. ")
