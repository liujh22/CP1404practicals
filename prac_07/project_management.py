"""
Estimate Time: 1 hour

Program to set and edit your projects!
Menu:
Load Project
Save ...
Display ...
Filter ... by date
Add new ...
Update project ...

"""
import datetime
from prac_07.project import Project


MENU = ("- (L)oad projects \n- (S)ave projects\n- (D)isplay projects "
        "\n- (F)ilter projects by date\n- (A)dd new project \n- (U)pdate project\n- (Q)uit")
FILENAME = "Projects.txt"


def main():
    """Main Menu"""
    projects = []
    read_file(FILENAME, projects)  # Read "projects.txt" as default input
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":

        # Load Project
        if choice == "l":
            filename = input("File name: ")
            read_file(filename, projects)

        # Save Project (Disabled)
        elif choice == "s":
            pass

        # Display Projects
        elif choice == "d":
            # sort before display
            sort_projects = sorted(projects, key=lambda x: x.priority)
            print_incomplete_projects(sort_projects)
            print()
            print_complete_projects(sort_projects)

        # Filter Projects by Date
        elif choice == "f":
            # sort before filtering
            sort_projects = sorted(projects, key=lambda x: x.priority)
            filter_date = get_filter()
            print_filtered(filter_date, sort_projects)

        # Add new projects
        elif choice == "a":
            print("Let's add a new project")
            new_project = create_project()
            projects.append(new_project)

        # Update existed Project
        elif choice == "u":
            print_index(projects)
            collect_changes(projects)

        # Unexpected choices
        else:
            print("Invalid input")
        print()
        print(MENU)
        choice = input(">>> ").lower()

    print("Thank you for using custom-built project management software.")


def print_filtered(filter_date, sort_projects):
    """comparing and filtering"""
    for project in sort_projects:
        if datetime.datetime.strptime(project.date, "%d/%m/%Y").date() >= filter_date:
            print(project)


def get_filter():
    """get filter date from user"""
    filter_date = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(filter_date, "%d/%m/%Y").date()  # change class
    return filter_date


def print_complete_projects(sort_projects):
    """print sorted list (complete)"""
    print("Completed projects:")
    for project in sort_projects:
        if project.is_complete():
            print(f"\t{project}")


def print_incomplete_projects(sort_projects):
    """print sorted list (incomplete)"""
    print("Incomplete projects:")
    for project in sort_projects:
        if not project.is_complete():
            print(f"\t{project}")


def collect_changes(projects):
    """gather valid changes"""
    update_choice = int(input("Project choice: "))
    print(projects[update_choice])
    new_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))
    if new_percentage != "":
        projects[update_choice].completion = new_percentage
    if new_priority != "":
        projects[update_choice].priority = new_priority


def print_index(projects):
    """Print projects' index and content"""
    for i, project in enumerate(projects):
        print(i, project)


def create_project():
    """Gather information for new project"""
    name = input("Name: ")
    date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = int(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    new_project = Project(name, date, priority, cost, completion)
    return new_project


def read_file(filename, projects):
    """read file and add projects to list"""
    with open(filename, encoding="utf-8") as in_file:
        in_file.readline()
    # Each line is a project
        for line in in_file:
            parts = line.strip().split("\t")
            # Name, Start Date, Priority, Cost Estimate, Completion Percentage
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)


main()
