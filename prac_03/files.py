name = input("Please enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()


file = open("name.txt", "r")
name = file.read().strip()
file.close()
print(f"Hi {name}!")
