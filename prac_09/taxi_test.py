"""
Client code to test Taxi.py
"""

from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100)  # Create new taxi
my_taxi.drive(40)  # Drive 40km
print(my_taxi)  # Print taxi detail
print(f"Your price is {my_taxi.get_fare()}")  # Print current fare
my_taxi.start_fare()  # Start new fare
my_taxi.drive(100)  # Drive 100km
print(my_taxi)  # Print taxi detail
print(f"Your price is {my_taxi.get_fare()}")  # Print current fare
