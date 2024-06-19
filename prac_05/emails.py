NAME_AND_EMAIL = {}

def main():
    email = input("Email: ")
    check_email(email)
    while email != "":
        check_email(email)
        user_name = get_user_name(email)
        check_user_name(user_name, email)
        email = input("Email: ")

    for name, email in NAME_AND_EMAIL.items():
        print(f"{name.title()} ({email})")

def check_email(email):
    while "@" not in email:
        print("Invalid email")
        email = input("Email: ")
        return email
    return email