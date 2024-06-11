numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("\nYou entered these numbers:")
for num in numbers:
    print(f"Number: {num}")


print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")


print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")

average = sum(numbers) / len(numbers)
print(f"The average of the numbers is {average:.1f}")

username = input("Enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
