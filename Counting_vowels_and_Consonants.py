class StringAnalyzer:
    def count_vowels_consonants(self, input_string):
        """
        Count the number of vowels and consonants in a given string.
        :param input_string: str - The string to be analyzed
        :return: tuple - (number of vowels, number of consonants)
        """
        vowels = "aeiouAEIOU"
        num_vowels = sum(1 for char in input_string if char in vowels)
        num_consonants = sum(1 for char in input_string if char.isalpha() and char not in vowels)

        return num_vowels, num_consonants


# Example usage
analyzer = StringAnalyzer()
input_str = "Hello, World!"

vowels, consonants = analyzer.count_vowels_consonants(input_str)
print(f"Vowels: {vowels}, Consonants: {consonants}")
