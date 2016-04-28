"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

numbers = []

with open('numbers.txt') as f:
    numbers = [int(line.strip()) for line in f]


print(sum(numbers))