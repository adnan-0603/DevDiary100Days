"""
Count words in string using class
-solved by Adnan
"""


class WordCounter:
    def __init__(self, string):
        self.string = string

    def count_words(self):
        # Splitting the string by spaces and counting the words
        return len(self.string.split())


# Example usage
string = "Hello, this is an example string."
word_counter = WordCounter(string)
number_of_words = word_counter.count_words()

print("Number of words:", number_of_words)
