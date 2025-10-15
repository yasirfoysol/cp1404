"""
CP1404 | Practical 04 | Subject Reader
Reads subject data from file and displays formatted output.
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subjects()
    display_subjects(subjects)


def load_subjects():
    """Load subject data from file into a list of lists."""
    subjects = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])  # Convert student number to int
            subjects.append(parts)
    return subjects


def display_subjects(subjects):
    """Display subject information nicely formatted."""
    for subject_code, lecturer, students in subjects:
        print(f"{subject_code} is taught by {lecturer} and has {students:3} students")


if __name__ == "__main__":
    main()
