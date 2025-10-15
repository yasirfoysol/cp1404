"""
CP1404 | Practical 03 | Exceptions Demo
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator again: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid integers!")
print("Finished.")

# Q1: ValueError occurs when user enters a non-integer.
# Q2: ZeroDivisionError occurs if denominator = 0.
# Q3: We can avoid ZeroDivisionError by checking denominator before dividing.
