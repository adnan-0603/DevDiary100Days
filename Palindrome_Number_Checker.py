"""
PALINDROME NUMBER CHECKER
-SOLVED BY ADNAN
"""


class PalindromeChecker:
    def __init__(self, number):
        self.number = number

    def is_palindrome(self):
        """
        Checks if the number is a palindrome.

        Returns:
            bool: True if the number is a palindrome, False otherwise.
        """
        # Convert the number to string to check for palindrome
        num_str = str(self.number)

        # Compare the string with its reverse
        return num_str == num_str[::-1]


# Example usage
number = 12321
checker = PalindromeChecker(number)
result = checker.is_palindrome()

print(f"The number {number} is a palindrome: {result}")
