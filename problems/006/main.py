"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


# Uses Faulhaber's formula (Grabbed from wikipedia)
def sum_of_squares(n):
    return int(n * (n + 1) * (2 * n + 1) / 6.0)


def square_of_sum(n):
    sum = int(n * (n + 1) / 2.0)
    return sum * sum


print(square_of_sum(100) - sum_of_squares(100))
