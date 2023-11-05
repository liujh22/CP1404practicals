"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Get data and print them"""
    data = get_data()
    print(data)
    print("----------")
    display_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    total = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        total.append(parts)
    input_file.close()
    return total


def display_data(data):
    """ Display data line by line """
    for lists in data:
        subject = lists[0]
        instructor = lists[1]
        number_of_students = lists[2]
        print(f"{subject} is taught by {instructor:<12} and has {number_of_students:>3} students")


main()
