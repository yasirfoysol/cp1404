"""CP1404/CP5632 Practical - Car class."""

class Car:
    """Represent a car object."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance.

        name: str, name of the car
        fuel: int, amount of fuel in units
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return string representation of the car."""
        return f"{self.name}, fuel={self.fuel}, odo={self.odometer}"

    def add_fuel(self, amount):
        """Add given amount of fuel to the car."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance if enough fuel.

        Returns: the actual distance driven.
        """
        if distance < 0:
            raise ValueError("Distance must be >= 0")
        if distance > self.fuel:
            distance = self.fuel
        self.odometer += distance
        self.fuel -= distance
        return distance
