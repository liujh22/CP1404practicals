"""
Client code for unreliable car
"""

from prac_09.unreliable_car import UnreliableCar
my_car = UnreliableCar("Mr. Hi", 100, 50)  # Create new taxi
print(my_car)  # Print taxi detail

my_car.drive(40)  # Drive 40km

print(my_car)  # Print taxi detail
