# -*- coding: utf-8 -*-
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""


from math import sqrt
from functools import reduce


def factorize(n, factors=None):
    if not factors:
        factors = set()
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            return factorize(n // x, factors)
    factors.add(n)
    return factors


def generate_multiples(n, max):
    return [n*x for x in range(1, max) if n*x < max]


def divisors(n):
    divisors = []
    for item in factorize(n):
        divisors += generate_multiples(item, n)
    return [1] + divisors


print(divisors(220))
