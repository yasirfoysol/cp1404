"""
CP1404 | Practical 04 | List Comprehensions
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Example list comprehensions
squares = [n ** 2 for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 != 0]
greater_than_5 = [n for n in numbers if n > 5]

# TODO tasks (complete)
lowercase_names = ["bob", "jim", "cat", "sue"]
upper_names = [name.upper() for name in lowercase_names]

# Extract numbers greater than 50 from mixed list
mixed_numbers = [3, 44, 56, 78, 23, 89, 12]
numbers_over_50 = [num for num in mixed_numbers if num > 50]

print(squares)
print(evens)
print(upper_names)
print(numbers_over_50)
