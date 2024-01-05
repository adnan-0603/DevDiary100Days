"""
Sort a string
-solved By Adnan
"""


def sort_string(s):
    # Sort the characters of the string and join them back into a string
    sorted_chars = sorted(s)
    sorted_string = ''.join(sorted_chars)
    return sorted_string

# Example usage
input_string = "hello"
sorted_string = sort_string(input_string)
print("Original string:", input_string)
print("Sorted string:", sorted_string)
