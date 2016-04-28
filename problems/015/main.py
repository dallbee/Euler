"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20x20 grid?
"""



# I've only been able to partially crack the pattern.
# There should be a closed form solution, but this will have to do:

n = 20

paths = [i for i in range(1, n+2)]

for _ in range(1, n):
    for i in range(1, n+1):
        paths[i] = paths[i] + paths[i-1]

print(paths[-1])
