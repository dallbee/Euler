"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt


def factorize(n):
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            return {x} | factorize(n // x)
    return {n}


print(max(factorize(600851475143)))
