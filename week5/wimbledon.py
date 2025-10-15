"""
CP1404 | Practical 05 | Wimbledon Data
Estimate: 40 minutes
Actual:   35 minutes
"""
FILENAME = "wimbledon.csv"


def main():
    """Display Wimbledon champions and countries."""
    data = load_data(FILENAME)
    champions_to_count = count_champions(data)
    countries = extract_countries(data)
    display_results(champions_to_count, countries)


def load_data(filename):
    """Read Wimbledon data file and return list of records."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # skip header
        for line in in_file:
            parts = line.strip().split(',')
            records.append(parts)
    return records


def count_champions(data):
    """Count how many times each champion has won."""
    champion_count = {}
    for record in data:
        champion = record[2]
        champion_count[champion] = champion_count.get(champion, 0) + 1
    return champion_count


def extract_countries(data):
    """Extract a sorted set of unique country codes."""
    return sorted({record[1] for record in data})


def display_results(champions_to_count, countries):
    """Display formatted results."""
    print("Wimbledon Champions:")
    for name, wins in champions_to_count.items():
        print(f"{name:20} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()
