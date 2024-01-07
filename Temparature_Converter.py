"""
-Temparature Converter
-solved by Adnan
"""


class TemperatureConverter:

    def celsius_to_fahrenheit(self, celsius):
        """Converts Celsius to Fahrenheit."""
        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        """Converts Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5 / 9

    def celsius_to_kelvin(self, celsius):
        """Converts Celsius to Kelvin."""
        return celsius + 273.15

    def kelvin_to_celsius(self, kelvin):
        """Converts Kelvin to Celsius."""
        return kelvin - 273.15

    def fahrenheit_to_kelvin(self, fahrenheit):
        """Converts Fahrenheit to Kelvin by first converting to Celsius."""
        return self.celsius_to_kelvin(self.fahrenheit_to_celsius(fahrenheit))

    def kelvin_to_fahrenheit(self, kelvin):
        """Converts Kelvin to Fahrenheit by first converting to Celsius."""
        return self.celsius_to_fahrenheit(self.kelvin_to_celsius(kelvin))


# Example usage
converter = TemperatureConverter()
celsius = 25
fahrenheit = converter.celsius_to_fahrenheit(celsius)
kelvin = converter.celsius_to_kelvin(celsius)

print(f"{celsius}°C is {fahrenheit}°F and {kelvin}K")
