"""Read programming languages from a file into ProgrammingLanguage objects.

Estimate: 15 minutes
Actual: X minutes
"""

from programming_language import ProgrammingLanguage


def load_languages(filename="languages.csv"):
    """Load languages from CSV file and return list of ProgrammingLanguage objects."""
    languages = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # Skip header
        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) != 5:
                continue
            name, typing, reflection_text, pointer_text, year_text = parts
            reflection = reflection_text.lower() == "yes"
            pointer_arithmetic = pointer_text.lower() == "yes"
            year = int(year_text)
            languages.append(
                ProgrammingLanguage(name, typing, reflection, pointer_arithmetic, year)
            )
    return languages


def main():
    """Display loaded languages."""
    languages = load_languages()
    for language in languages:
        print(language)


if __name__ == "__main__":
    main()
