import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBER_IN_LINE = 6

# line_number = int(input("How many quick picks? "))
# numbers = []
# for i in range(0, line_number):
#     numbers.clear()
#     for g in range(0, 6):
#         pick_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
#         while pick_number in numbers:
#             pick_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
#         numbers.append(pick_number)
#         numbers.sort()
#     print(" ".join(f"{number:2}" for number in numbers))
line_num = int(input("how many line:"))
for line in range(line_num):
    count_to_6 = 0
    numbers = []
    while count_to_6 < 6:
        number = random.randint(1,45)
        if not number in numbers:
            numbers.append(number)
            count_to_6 += 1
    print(" ".join(sorted(f"{str(num):>2}" for num in numbers)))
