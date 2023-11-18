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
import datetime
from prac_07.project import Project


MENU = ("- (L)oad projects \n- (S)ave projects\n- (D)isplay projects "
        "\n- (F)ilter projects by date\n- (A)dd new project \n- (U)pdate project\n- (Q)uit")
FILENAME = "Projects.txt"


def main():
    projects = []
    read_file(FILENAME, projects)
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("File name: ")
            read_file(filename, projects)

        elif choice == "s":
            pass

        elif choice == "d":
            sort_projects = sorted(projects, key=lambda x: x.priority)
            print("Incomplete projects:")
            for project in sort_projects:
                if not project.is_complete():
                    print(f"\t{project}")
            print("Completed projects:")
            for project in sort_projects:
                if project.is_complete():
                    print(f"\t{project}")

        elif choice == "f":
            filter_date = input("Show projects that start after date (dd/mm/yy): ")
            filter_date = datetime.datetime.strptime(filter_date, "%d/%m/%Y").date()
            for project in projects:
                if datetime.datetime.strptime(project.date, "%d/%m/%Y").date() >= filter_date:
                    print(project)

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
            for i, project in enumerate(projects):
                print(i, project)
            update_choice = int(input("Project choice: "))
            print(projects[update_choice])
            new_percentage = int(input("New Percentage: "))
            new_priority = int(input("New Priority: "))
            if new_percentage != "":
                projects[update_choice].completion = new_percentage
            if new_priority != "":
                projects[update_choice].priority = new_priority

        else:
            print("Invalid input")
        print()
        print(MENU)
        choice = input(">>> ").lower()

    print("Thank you for using custom-built project management software.")


def read_file(filename, projects):
    in_file = open(filename, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()


main()
