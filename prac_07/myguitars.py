import csv
from guitar import Guitar

def main():
    filename = "guitars.csv"
    guitars = read_guitars(filename)

    guitars.sort()
    print_guitars(guitars)

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




main()