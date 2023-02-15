"""Practicing Functions"""


def my_max(number1: int, number2: int) -> int:
    """Returns the max value of 2 numbers"""
    if number1 >= number2:
        return number1
    else: #if number2 >= number1
        return number2

max_number: int = my_max(1,100)
print(max_number)
