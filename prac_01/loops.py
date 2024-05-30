for i in range(1, 21, 2):
    print(i, end=' ')
print()
# (Question a)
print("Question a:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# (Question b)
print("\nQuestion b:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# (Question c)
print("\nQuestion c:")
num_stars = int(input("Number of stars: "))
for _ in range(num_stars):
    print('*', end='')
print()

# （Question d）
print("\nQuestion d:")
num_stars = int(input("Number of stars: "))
for i in range(1, num_stars + 1):
    print('*' * i)
