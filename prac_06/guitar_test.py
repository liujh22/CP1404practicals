from prac_06.guitar import Guitar


def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(guitar1)
    print(guitar1.get_age())
    print(guitar1.is_vintage())


main()
