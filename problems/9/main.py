"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt
from functools import reduce

def find_triple(x):
    for a in range(1, x):
        b = (x * (a - .5*x))/(a - x)
        if b == int(b):
            return map(int, (a, b, sqrt(a*a + b*b)))

print(reduce(lambda x, y: x*y, find_triple(1000)))


