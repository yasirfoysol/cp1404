"""
CP1404 | Practical 04 | Total Income Calculator
"""
def main():
    """Calculate monthly cumulative incomes and display formatted report."""
    number_of_months = int(input("How many months? "))
    incomes = []
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Display income report showing cumulative totals."""
    print("\nIncome Report")
    print("-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


if __name__ == "__main__":
    main()
