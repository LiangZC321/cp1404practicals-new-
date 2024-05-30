def main():
    password = get_password()
    print_password_asterisks(password)

def get_password():
    min_length = 7
    password = input("Please enter your password:")

    while len(password) < min_length:
        print("Invalid password. At least 7 characters long.")
        password = input("Please enter your password:")

    return password