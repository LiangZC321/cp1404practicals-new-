import csv


def main():
    filename = "wimbledon.csv"
    information = read_file(filename)
    champions_to_times, champion_countries = organize_information(information)
    display_summy(champions_to_times, champion_countries)

def read_file(filename):
    information = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            information.append(row)
    return information

def organize_information(information):
    champions_to_times = {}
    champion_countries = set()

    for row in information:
        champion = row[2]
        country = row[1]

        champions_to_times[champion] = champions_to_times.get(champion, 0) + 1
        champion_countries.add(country)
    return champions_to_times, sorted(champion_countries)

def display_summy(champions_to_times, champion_countries):
    print("Wimbledon Champions:")
    for champions, times in champions_to_times.items():
        print(f"{champions} {times}")

    print("These countries have won Wimbledon:")
    countries = ", ".join(champion_countries)
    print(countries)


main()