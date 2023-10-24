

MENU = """G - Get a valid score (must be 0-100 inclusive)
P - Print result (copy or import your function to determine the result from score.py)
S - Show stars (this should print as many stars as the score)
Q - Quit"""


def main():
    score = 101
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            status = determine_status(score)
            print(f"Your status is {status}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print()
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you")


def get_valid_score():
    score = int(input("Enter a score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter a score: "))
    return score


def determine_status(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    if score < 0 or score > 100:
        print("Your have a Invalid score")
    else:
        print("*" * score)


main()
