"""
CP1404 | Practical 05 | State Names
"""

STATE_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

def main():
    """Display state names and look up abbreviations."""
    for abbr, name in STATE_NAMES.items():
        print(f"{abbr:3} is {name}")
    print()

    state = input("Enter short state: ").upper()
    while state != "":
        try:
            print(f"{state} is {STATE_NAMES[state]}")
        except KeyError:
            print("Invalid short state")
        state = input("Enter short state: ").upper()


if __name__ == "__main__":
    main()
