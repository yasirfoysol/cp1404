"""Project class for Project Management Program.

Estimate: 20 minutes
Actual: X minutes
"""

from datetime import date


class Project:
    """Represent a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """Initialise a Project.

        start_date: datetime.date
        priority: int
        cost_estimate: float
        completion: int (0-100)
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion}%")

    def is_complete(self):
        """Return True if project is 100% complete."""
        return self.completion >= 100

    def __lt__(self, other):
        """Order by priority, then start date."""
        if self.priority == other.priority:
            return self.start_date < other.start_date
        return self.priority < other.priority
