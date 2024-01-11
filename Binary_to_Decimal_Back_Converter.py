class BinaryDecimalConverter:
    def binary_to_decimal(self, binary_str):
        """
        Convert a binary string to a decimal number.
        :param binary_str: str - binary string like '1011'
        :return: int - decimal representation
        """
        return int(binary_str, 2)

    def decimal_to_binary(self, decimal_num):
        """
        Convert a decimal number to a binary string.
        :param decimal_num: int - decimal number like 11
        :return: str - binary representation
        """
        return bin(decimal_num)[2:]


# Example usage
converter = BinaryDecimalConverter()
binary_number = "1011"
decimal_number = 22

# Convert binary to decimal
converted_decimal = converter.binary_to_decimal(binary_number)
# Convert decimal to binary
converted_binary = converter.decimal_to_binary(decimal_number)

print(converted_decimal, converted_binary)
