"""
Estimate Time: 1 hour

Menu:
Load Project
Save Projects
Display
Filter by date
add new
 update project

"""
from prac_07.project import Project

MENU = ("- (L)oad projects \n- (S)ave projects\n- (D)isplay projects "
        "\n- (F)ilter projects by date\n- (A)dd new project \n- (U)pdate project\n- (Q)uit")


def main():
    projects = []
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            pass
        elif choice == "s":
            pass
        elif choice == "d":
            pass
        elif choice == "f":
            pass
        elif choice == "a":
            print("Let's add a new project")
            name = input("Name: ")
            date = input("Start date (dd/mm/yy): ")
            priority = int(input("Priority: "))
            cost = int(input("Cost estimate: $"))
            completion = int(input("Percent complete: "))
            new_project = Project(name, date, priority, cost, completion)
            projects.append(new_project)


        elif choice == "u":
            pass
        else:
            print("Invalid input")

        print(MENU)
        choice = input(">>> ").lower()

    print("Thank you for using custom-built project management software.")


main()
