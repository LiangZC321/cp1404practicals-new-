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

def get_user_name(email):
    users_information = email.split("@")[0].split('.')
    user_name = ' '.join(information.title() for information in users_information)
    return user_name