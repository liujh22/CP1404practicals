"""
Test code for silver service taxi
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Hummer", 200, 4)
my_taxi.drive(9)
print(my_taxi)
print(f"{my_taxi.get_fare():.2f}")
