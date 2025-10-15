"""
CP1404 | Practical 03 | String Formatting
"""

# 1. f-string formatting
name = "Gibson L-5 CES"
year = 1922
cost = 16036
print(f"{year} {name} for about ${cost:,.0f}!")

# 2. Range and alignment using f-string formatting
for i in range(11):
    print(f"2 ^ {i:2} is {2 ** i:5}")
