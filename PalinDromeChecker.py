"""
Palindrome Checker: Write a function to check if a string is a palindrome (reads the same backward as forward).
-solved by Adnan
"""


def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    clean_str = ''.join(char.lower() for char in s if char.isalnum())

    # Initialize pointers for the start and end of the string
    start, end = 0, len(clean_str) - 1

    # Check for palindrome by comparing characters
    while start < end:
        if clean_str[start] != clean_str[end]:
            # If characters don't match, it's not a palindrome
            return False
        start += 1
        end -= 1

    # If all characters match, it's a palindrome
    return True


# Test cases
print(is_palindrome("Adnan"))  # False
print(is_palindrome("racer"))  # False
print(is_palindrome("nan"))  # True
