"""
CP1404 | Practical 03 | Random Numbers
"""
import random

# Run these multiple times to observe different results
print(random.randint(5, 20))   # Smallest: 5, Largest: 20
print(random.randrange(3, 10, 2))  # Possible: 3, 5, 7, 9 (cannot produce 4)
print(random.uniform(2.5, 5.5))  # Range: 2.5 ≤ x ≤ 5.5

# Random number between 1 and 100 inclusive
print(random.randint(1, 100))
