# """
# CP1404/CP5632 Practical
# Data file -> lists program
# """
#
# FILENAME = "subject_data.txt"
#
#
# def main():
#     data = get_data()
#     print(data)
#     display_new_data()
#
#
# def get_data():
#     """Read data from file formatted like: subject,lecturer,number of students."""
#     teachers_information = []
#     input_file = open(FILENAME, 'r')
#     for line in input_file:
#         # print(line)  # See what a line looks like
#         # print(repr(line))  # See what a line really looks like
#         line = line.strip()  # Remove the \n
#         parts = line.split(',')  # Separate the data into its parts
#         # print(parts)  # See what the parts look like (notice the integer is a string)
#         parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
#         teachers_information.append(parts)
#         # print(parts)  # See if that worked
#         # print("----------")
#     input_file.close()
#     return teachers_information
#
#
# def display_new_data():
#     input_file = open(FILENAME, 'r')
#     for line in input_file:
#         line = line.strip()
#         parts = line.split(',')
#         print(f"{parts[0]} is taught by {parts[1]}and has {parts[2]} students")
#     input_file.close()
#
#
# main()

FILENAME = "subject_data.txt"


def get_status():
    """
    CP1401 is taught by Ada Lovelace and has 192 students
CP1404 is taught by Alan Turing  and has  98 students
    """
    with open(FILENAME, "r") as file:
        for line in file:
            line.strip()
            items_in_line = line.split(",")
            print(f"{items_in_line[0]} is taught by {items_in_line[1]} and has {items_in_line[2]} students")



def main():
    load_data()
    get_status()



def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
    input_file.close()


main()