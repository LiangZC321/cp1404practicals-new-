from guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = "(vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth ${guitar.cost:,.2f} {vintage_string}")
    else:
        print("No guitars :( Maybe buy one?")


if __name__ == "__main__":
    main()
