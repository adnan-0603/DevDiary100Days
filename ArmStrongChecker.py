class ArmstrongChecker:
    def count_digits(self, number):
        """" Count the number of digits in the given number """
        return len(str(number))

    def is_armstrong(self, number):
        """" Check if the given number is an Armstrong Number """
        num_digits = self.count_digits(number)
        sum_of_powers = sum(int(digit) ** num_digits for digit in str (number))
        return sum_of_powers == number

    #Example of Usage

    checker = ArmstrongChecker()
    number_to_check = 153
    if checker.is_armstrong(number_to_check):
        print(f"{number_to_check} is an Armstrong number.")
    else:
        print(f"{number_to_check} is not an Armstrong number.")
