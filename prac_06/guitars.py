"""
Input guitars and list them!
"""
from prac_06.guitar import Guitar


def main():
    """Main Program"""
    print("My guitars!")
    name = input("Name: ")
    guitars = []
    input_guitar(guitars, name)

    # Testing
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))

    guitars.sort(key=lambda x: x.year)
    print_guitar_list(guitars)


def print_guitar_list(guitars):
    """print guitar list, if not print warning"""
    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print(f"Guitar {i}: "
                  f"{guitar.name:>20} "
                  f"({guitar.year}), "
                  f"worth ${guitar.cost:10,.2f}"
                  f"{vintage_string}")
    else:
        print("No guitars :( Quick, go and buy one!")


def input_guitar(guitars, name):
    """Menu to get input"""
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.")
        name = input("Name: ")


main()
