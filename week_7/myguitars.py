"""My Guitars - load, display, add, and save guitars.

Estimate: 25 minutes
Actual: X minutes
"""

from guitar import Guitar


FILENAME = "guitars.csv"


def main():
    """Load guitars from file, display, allow user to add, then save."""
    guitars = load_guitars(FILENAME)

    print("These are my guitars:")
    display_guitars(guitars)

    print("\nAdd new guitars (blank name to stop):")
    guitars = add_new_guitars(guitars)

    guitars.sort()  # uses Guitar.__lt__
    print("\nSorted guitars:")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print(f"\nGuitars saved to {FILENAME}.")


def load_guitars(filename):
    """Load guitars from CSV and return list of Guitar objects."""
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue
            name, year_text, cost_text = parts
            guitars.append(Guitar(name, int(year_text), float(cost_text)))
    return guitars


def display_guitars(guitars):
    """Display guitars with formatting."""
    for i, guitar in enumerate(guitars, 1):
        vintage_tag = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
              f"worth ${guitar.cost:10,.2f}{vintage_tag}")


def add_new_guitars(guitars):
    """Prompt user to add new guitars."""
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
    return guitars


def save_guitars(filename, guitars):
    """Save guitars back to CSV file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
