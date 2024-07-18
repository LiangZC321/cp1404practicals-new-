from guitar import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    guitars.sort()

    for guitar in guitars:
        print(guitar)

    add_guitar(guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)