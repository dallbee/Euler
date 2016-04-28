"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def generate_multiples(n, max):
    return (n*x for x in range(1, max//n + 1))


def sieve(n):
    primes = [2]
    taken = set(generate_multiples(2, n))
    for x in range(3, n, 2):
        if x not in taken:
            primes.append(x)
            taken |= set(generate_multiples(x, n))
    return primes


print(sum(sieve(2000000)))