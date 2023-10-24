def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password = input("Enter your password: ")
    while len(password) < 10:
        print("Too Short")
        password = input("Enter your password: ")
    return password


def print_asterisks(the_password):
    password_length = len(the_password)
    for i in range(password_length):
        print("*", end="")


main()
