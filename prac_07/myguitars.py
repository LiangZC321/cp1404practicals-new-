import csv
from guitar import Guitar

def main():
    filename = "guitars.csv"
    guitars = read_guitars(filename)
    guitars = add_new_guitars(guitars)

    guitars.sort()
    print_guitars(guitars)
    write_guitars(filename, guitars)

def read_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                name, year, cost = row
                guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def print_guitars(guitars):
    for guitar in guitars:
        print(guitar)

def add_new_guitars(guitars):
    print("Enter your new guitars(space to stop):")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
    return guitars

def write_guitars(filename, guitars):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])



main()