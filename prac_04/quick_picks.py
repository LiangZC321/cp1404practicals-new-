import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBER_IN_LINE = 6

line_number = int(input("How many quick picks? "))
numbers = []
for i in range(0, line_number):
    numbers.clear()
    for g in range(0, 6):
        pick_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while pick_number in numbers:
            pick_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        numbers.append(pick_number)
        numbers.sort()
    print(" ".join(f"{number:2}" for number in numbers))