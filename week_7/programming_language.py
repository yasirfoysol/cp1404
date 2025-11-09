"""Programming Language class with pointer arithmetic.

Estimate: 10 minutes
Actual: X minutes
"""


class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name, typing, reflection, pointer_arithmetic, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing                    # "Static" / "Dynamic"
        self.reflection = reflection            # bool
        self.pointer_arithmetic = pointer_arithmetic  # bool
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return string representation."""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, "
                f"Pointer arithmetic={self.pointer_arithmetic}, "
                f"First appeared in {self.year}")
