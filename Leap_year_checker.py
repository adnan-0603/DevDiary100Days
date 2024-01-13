"""
Leap Year
-Solved By Adnan
"""


class LeapYearChecker:
    def __init__(self, year):
        self.year = year

    def is_leap_year(self):
        # Leap years are divisible by 4
        if self.year % 4 == 0:
            # But if a year is divisible by 100, it is NOT a leap year
            # unless it is also divisible by 400
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


# Example usage
year_to_check = 2024
checker = LeapYearChecker(year_to_check)
if checker.is_leap_year():
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")
