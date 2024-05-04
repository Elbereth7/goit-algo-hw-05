import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[str, None, None]:
# Finding all the real numbers in string and returning them as generator
    pattern = r" \d+\.*\d* " # Using regex to identify all real numbers in string - both decimals and integers.
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield number # Returning generator

def sum_profit(text: str, func: Callable[[str], Generator[str, None, None]]) -> float:
# Counting sum of all numbers returned by a numbers generator
    sum = 0
    for number in func(text):
        sum += float(number)
    return sum

if __name__ == '__main__':
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
