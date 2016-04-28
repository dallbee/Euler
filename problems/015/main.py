"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20x20 grid?
"""

from functools import reduce

print(reduce(lambda x, y: int(x) + int(y), str(pow(2, 1000))))