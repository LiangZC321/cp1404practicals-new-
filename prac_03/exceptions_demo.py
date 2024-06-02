"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
have an input that not an int
2. When will a ZeroDivisionError occur?
enter the value of denominator with 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
I do
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")