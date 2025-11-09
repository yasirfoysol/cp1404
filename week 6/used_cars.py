"""CP1404/CP5632 Practical - Client code using the Car class."""

from car import Car


def main():
    """Demo cars."""
    # Existing example cars
    bus = Car("Bus", 180)
    bus.drive(30)
    print(bus)

    # New limo example
    limo = Car("Limo", 100)          # 1) create with 100 fuel
    limo.add_fuel(20)                # 2) add 20 fuel
    print(limo.fuel)                 # 3) print fuel amount
    limo.drive(115)                  # 4) attempt to drive 115 km
    print(limo)                      # Check __str__ with name/odo/fuel


if __name__ == "__main__":
    main()
