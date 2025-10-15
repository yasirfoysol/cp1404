"""
CP1404 | Practical 03 | Capitalist Conrad
Stock price simulator with file output
"""
import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "stock_prices.txt"

price = INITIAL_PRICE
number_of_days = 0

out_file = open(FILENAME, 'w')
print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = -random.uniform(0, MAX_DECREASE)
    price *= (1 + price_change)
    number_of_days += 1
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

out_file.close()
print(f"Simulation complete after {number_of_days} days. Results in {FILENAME}")
