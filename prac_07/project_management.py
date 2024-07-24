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

def load_projects(filename):
    projects = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)
        for row in reader:
            if row:
                projects.append(Project(*row))
    return projects

def save_projects(filename, projects):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'), project.priority, project.cost_estimate, project.completion_percentage])

def display_projects(projects):
    incomplete = [p for p in projects if p.completion_percentage < 100]
    completed = [p for p in projects if p.completion_percentage == 100]
    print("Incomplete projects:")
    for project in sorted(incomplete, key=lambda x: x.priority):
        print(f"  {project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, priority {project.priority}, estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")
    print("Completed projects:")
    for project in sorted(completed, key=lambda x: x.priority):
        print(f"  {project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, priority {project.priority}, estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

def filter_projects_by_date(projects):
    input_date = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.strptime(input_date, "%d/%m/%Y")
    filtered = [p for p in projects if p.start_date > filter_date]
    for project in sorted(filtered, key=lambda x: x.start_date):
        print(f"{project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, priority {project.priority}, estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))

def update_project(projects):
    for idx, project in enumerate(projects):
        print(f"{idx} {project}")
    project_index = int(input("Project choice: "))
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")
    projects[project_index].update_completion(new_completion)
    projects[project_index].update_priority(new_priority)

main()