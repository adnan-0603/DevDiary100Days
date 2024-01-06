"""
Scientific Calculator
-solved by Adnan
"""
import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return None
    return x / y


def power(x, y):
    return math.pow(x, y)


def square(x):
    return math.sqrt(x)


def log(x, base=math.e):
    """Calculate the logarithm of x with given base. Default is natural log."""
    return math.log(x, base)


def print_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter choice(1/2/3/4/5/6/7/8): ")

        if choice == '8':
            break

        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
        elif choice == '6':
            num = float(input("Enter number: "))
            print("Result:", square(num))
        elif choice == '7':
            base = input("Enter base (default is e): ")
            base = float(base) if base else math.e
            num = float(input("Enter number: "))
            print("Result:", log(num, base))
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
