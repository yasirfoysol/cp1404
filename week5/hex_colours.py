"""
CP1404 | Practical 05 | Hex Colour Lookup
"""

COLOUR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "black": "#000000",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a",
    "cadetblue": "#5f9ea0"
}

def main():
    """Lookup hex colour codes."""
    colour_name = input("Enter colour name: ").lower()
    while colour_name != "":
        print(f"{colour_name} is {COLOUR_CODES.get(colour_name, 'Invalid colour name')}")
        colour_name = input("Enter colour name: ").lower()


if __name__ == "__main__":
    main()
