import csv


def main():
    filename = "wimbledon.csv"
    information = read_file(filename)
    champions_to_times, champion_countries = organize_information(information)
    display_summy(champions_to_times, champion_countries)