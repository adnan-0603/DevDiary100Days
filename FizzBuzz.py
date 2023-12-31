"""
FizzBuzz: Print numbers from 1 to 100, but for multiples of 3 print "Fizz" instead of the number,
and for multiples of 5 print "Buzz". For numbers which are multiples of both 3 and 5 print "FizzBuzz"
-solved by Adnan
"""


def fizz_buzz(n):
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# call the function
fizz_buzz(100)
