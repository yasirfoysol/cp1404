"""Client program for ProgrammingLanguage.

Estimate: 10 minutes
Actual: X minutes
"""

from programming_language import ProgrammingLanguage


def main():
    """Create and use ProgrammingLanguage objects."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Check __str__
    print(python)

    languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()
