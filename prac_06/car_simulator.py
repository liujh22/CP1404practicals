"""
Driving simulator using class of car
"""
from prac_06.car import Car

MENU = "Menu:\nd) drive\nr) refuel\nq) quit"


def main():
    """Menu program"""
    print("Let's drive!")
    name = input("Enter your car name: ")
    # create a car instance with initial fuel of 100 and user proviede name
    car = Car(name, fuel=100)
    print(car)
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            user_distance = int(input("How many km do you wish to drive? "))
            user_distance = check_distance(user_distance)
            actual_distance = car.drive(user_distance)
            print_distance(actual_distance, car)
        elif choice == "r":
            refuel = int(input("How many units of fuel do you want to add to the car? "))
            refuel = check_fuel_unit(refuel)
            car.add_fuel(refuel)
            print(f"Added {refuel} units of fuel.")
        else:
            print("Invalid choice")
        print(f"\n{car}")
        print(MENU)
        choice = input("Enter your choice: ").lower()

    print(f"\nGood bye {car.name}'s driver.")


def check_fuel_unit(refuel):
    """reject, if refuel < 0"""
    while refuel < 0:
        print("Fuel amount must be >= 0")
        refuel = int(input("How many units of fuel do you want to add to the car? "))
    return refuel


def print_distance(actual_distance, car):
    """print actual distance"""
    if car.fuel == 0:
        print(f"The car drove {actual_distance}km and ran out of fuel.")
    else:
        print(f"The car drove {actual_distance}km.")


def check_distance(user_distance):
    """reject, if distance <0"""
    while user_distance < 0:
        print("Distance must be >= 0")
        user_distance = int(input("How many km do you wish to drive? "))
    return user_distance


main()
