"""
Class of silver taxi
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.price_per_km = float(fanciness) * Taxi.price_per_km

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return (f"{super().__str__()}, "
                f"plus flagfall of ${self.flagfall:.2f}")
