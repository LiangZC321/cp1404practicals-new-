"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

MENU = """
(H)ello
(G)oodbye
(Q)uit
"""
# def main():
#     name = input("Enter name: ")
#     display_menu = True
#     while display_menu:
#         print(MENU)
#         choice = input(">>> ").upper()
#
#         if choice == "Q":
#             print("Finished.")
#             display_menu = False
#         elif choice == "H":
#             print("Hello", name)
#         elif choice == "G":
#             print("Goodbye", name)
#         else:
#             print("Invalid choice")
#
#
# if __name__ == "__main__":
#     main()

name = input("enter ur name: ").lower()
print(MENU)
choice = input("\n>>> ").lower()
while choice != "q":
    if choice == "h":
        print("Hello!")
    elif choice == "g":
        print("goodbye")
    else:
        print("invalid")
    print(MENU)
    choice = input("\n>>> ").lower()

print("all right")




