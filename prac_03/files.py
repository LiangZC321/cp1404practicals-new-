name = input("Please enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()