"""
CP1404 | Practical 03 | Exceptions To Complete
Safely get an integer from the user
"""
finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a number: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print(f"The result is: {result}")
