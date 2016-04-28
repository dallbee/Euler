"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def primes(n):
    primes = [2]
    x = 3
    while len(primes) < n:
        factor = None
        for p in primes:
            if x % p == 0:
                factor = x
                break
        if factor is None:
            primes.append(x)
        x += 2

    return primes


print(primes(10001)[-1])