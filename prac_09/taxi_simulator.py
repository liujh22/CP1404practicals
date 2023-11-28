"""
Client code of Taxi and SilverServiceTaxi
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Menu program of taking taxis"""
    taxi_list = create_taxi_list()
    choice, choose_taxi, total_cost = initialize_welcome_screen()
    while choice != "q":  # "q" to exit

        if choice == "c":  # "c" to choose taxi
            print("Taxis available:")
            print_taxi_list(taxi_list)
            taxi_number = int(input("Choose taxi: "))  # choose a taxi
            if taxi_number >= len(taxi_list):  # check availability
                print("Invalid taxi choice")
            else:
                choose_taxi = taxi_list[taxi_number]

        elif choice == "d":  # "d" to drive taxi
            if choose_taxi == "":  # check availability
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("Drive how far? "))
                choose_taxi.start_fare()
                choose_taxi.drive(distance)
                print(f"Your {choose_taxi.name} trip cost you ${choose_taxi.get_fare():.2f}")
                total_cost += choose_taxi.get_fare()
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    print_taxi_list(taxi_list)


def print_taxi_list(taxi_list):
    """Print taxis"""
    for i, taxis in enumerate(taxi_list):
        print(f"{i} - {taxi_list[i]}")


def initialize_welcome_screen():
    """Print menu and request input"""
    print("Let's drive")
    print(MENU)
    choice = input(">>> ").lower()
    choose_taxi = ""
    total_cost = 0
    return choice, choose_taxi, total_cost


def create_taxi_list():
    """Taxi list with 1 standard, 2 silver taxis"""
    Prius = Taxi("Prius", 100)
    Limo = SilverServiceTaxi("Limo", 100, 2)
    Hummer = SilverServiceTaxi("Hummer", 200, 4)
    taxi_list = [Prius, Limo, Hummer]
    return taxi_list


main()
