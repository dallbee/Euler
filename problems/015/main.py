"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20x20 grid?
"""

from math import factorial


def binomial_coefficient(a, b):
    return factorial(a)/(factorial(b)*factorial(a - b))


print(binomial_coefficient(40, 20))