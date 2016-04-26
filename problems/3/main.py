"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math


def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def factorize(n):
    primes = []
    for x in range(2, int(math.sqrt(n)), 2):
        if n % x == 0 and is_prime(x):
            primes.append(x)
    return primes


print(max(factorize(600851475143)))
