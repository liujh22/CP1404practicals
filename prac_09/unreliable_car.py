"""
Inherit from Car
"""
import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name="", fuel=0, car_reliability=0):
        """Initialise a Car instance.
        name: string, reference name for car
        fuel: float, one unit of fuel drives one kilometre
        reliability: float, between 0 and 100, that represents the percentage chance in drive method
        """
        self.car_reliability = car_reliability
        super().__init__(name, fuel)

    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        reliability = random.randint(0, 101)
        if self.car_reliability >= reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
        else:
            print("Break down, Unreliable car!")
        return distance

    price_per_km = 1.23
