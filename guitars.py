"""Store and display user's guitars.

Estimate: 20 minutes
Actual: X minutes
"""

from guitar import Guitar


def main():
    """Get guitars from user and display them."""
    print("My guitars!")
    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    # For faster testing, you can comment out input above and use:
    # guitars = [
    #     Guitar("Gibson L-5 CES", 1922, 16035.40),
    #     Guitar("Line 6 JTV-59", 2010, 1512.9),
    # ]

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
              f"worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()
