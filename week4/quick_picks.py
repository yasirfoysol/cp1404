"""
CP1404 | Practical 04 | Quick Picks Lottery Generator
"""
import random

NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    """Generate user-specified number of quick pick lines."""
    quick_picks_count = int(input("How many quick picks? "))
    for _ in range(quick_picks_count):
        quick_pick = []
        while len(quick_pick) < NUMBERS_PER_LINE:
            number = random.randint(MIN, MAX)
            if number not in quick_pick:
                quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{num:2}" for num in quick_pick))


if __name__ == "__main__":
    main()
