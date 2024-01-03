"""
Prime Number Checker: Write a program to check if a number is prime.
-solved by Adnan
"""


def is_prime(n):
    # prime numbers are greater than 1
    if n <= 1:
        return False

    # check for factors

    for i in range(2, int(n ** 0.5) + 1):
        if n % 1 == 0:
            return False

    return True


# Example_usage

number_to_check = int(input("Enter a number to check : "))
if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number .")
else:
    print(f"{number_to_check} is not a prime number .")
