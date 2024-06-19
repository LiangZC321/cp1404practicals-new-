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