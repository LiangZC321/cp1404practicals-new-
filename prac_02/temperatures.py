# def main():
#     celsius = float(input("Enter Celsius: "))
#     fahrenheit = celsius_to_fahrenheit(celsius)
#     print(f"{celsius}°C is {fahrenheit}°F")
#
#     fahrenheit = float(input("Enter Fahrenheit: "))
#     celsius = fahrenheit_to_celsius(fahrenheit)
#     print(f"{fahrenheit}°F is {celsius}°C")
#
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32
#
# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9
#
# main()

MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            Celsius = float(input("enter Celsius: "))
            Fahrenheit = convert_celsius_to_fahrenheit(Celsius)
            print(f"F = {Fahrenheit}")
        elif choice == "F":
            Fahrenheit = float(input("enter fahrenheit: "))
            Celsius =convert_fahrenheit_to_celsius(Fahrenheit)
            print(f"C = {Celsius}")
        else:
            print("invalid")
        print(MENU)
        choice = input(">>>").upper()
    print("that's it")

main()
