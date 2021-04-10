"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner. How
many such routes are there through a 20x20 grid?
"""
import math

N = 20
K = 20

routes = math.comb(N+K, K)
print(routes)
