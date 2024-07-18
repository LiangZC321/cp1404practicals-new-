import csv
from project import Project
from datetime import datetime

menu = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit"

def main():
    projects = load_projects('projects.txt')
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from projects.txt")
    while True:
        print(menu)
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            if input("Would you like to save to projects.txt? ").lower() in ['yes', 'y']:
                save_projects('projects.txt', projects)
            print("Thank you for using custom-built project management software.")
            break