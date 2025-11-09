"""Project Management Program.

Estimate: 40 minutes
Actual: X minutes
"""

from datetime import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"
DATE_FORMAT = "%d/%m/%Y"


def main():
    """Run the project management program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    menu = ("- (L)oad projects\n"
            "- (S)ave projects\n"
            "- (D)isplay projects\n"
            "- (F)ilter projects by date\n"
            "- (A)dd new project\n"
            "- (U)pdate project\n"
            "- (Q)uit")

    choice = ""
    while choice != "Q":
        print(menu)
        choice = input(">>> ").strip().upper()
        if choice == "L":
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
            print(f"Projects saved to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            save_choice = input(
                f"Would you like to save to {DEFAULT_FILENAME}? ").strip().lower()
            if save_choice.startswith("y"):
                save_projects(DEFAULT_FILENAME, projects)
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid choice")


def load_projects(filename):
    """Load projects from file and return list of Project objects."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            line = line.strip()
            if not line:
                continue
            name, start_text, priority_text, cost_text, completion_text = line.split("\t")
            start_date = datetime.strptime(start_text, DATE_FORMAT).date()
            priority = int(priority_text)
            cost_estimate = float(cost_text)
            completion = int(completion_text)
            projects.append(Project(name, start_date, priority, cost_estimate, completion))
    return projects


def save_projects(filename, projects):
    """Save projects to file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion", file=out_file)
        for project in projects:
            print(f"{project.name}\t"
                  f"{project.start_date.strftime(DATE_FORMAT)}\t"
                  f"{project.priority}\t"
                  f"{project.cost_estimate:.2f}\t"
                  f"{project.completion}", file=out_file)


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    completed = [p for p in projects if p.is_complete()]

    incomplete.sort()
    completed.sort()

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Display projects that start after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_string, DATE_FORMAT).date()
    filtered = [p for p in projects if p.start_date >= filter_date]
    filtered.sort(key=lambda p: p.start_date)
    for project in filtered:
        print(project)


def add_project(projects):
    """Add a new project from user input."""
    print("Let's add a new project")
    name = input("Name: ")
    start_text = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))

    start_date = datetime.strptime(start_text, DATE_FORMAT).date()
    projects.append(Project(name, start_date, priority, cost_estimate, completion))


def update_project(projects):
    """Update an existing project's completion and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
    except (ValueError, IndexError):
        print("Invalid project choice")
        return

    print(project)
    new_completion = input("New Percentage (leave blank to skip): ")
    if new_completion.strip():
        project.completion = int(new_completion)

    new_priority = input("New Priority (leave blank to skip): ")
    if new_priority.strip():
        project.priority = int(new_priority)


if __name__ == "__main__":
    main()
