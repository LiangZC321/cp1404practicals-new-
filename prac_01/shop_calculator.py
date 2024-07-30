DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.9

# def main():
#     number_items = int(input("Number of items: "))
#
#     if number_items >= 0:
#         total_price = 0
#         for i in range(number_items):
#             price = float(input("Price of item: "))
#             total_price += price
#
#         if total_price > DISCOUNT_THRESHOLD:
#             total_price *= DISCOUNT_RATE
#
#         print(f"Total price for {number_items} items is ${total_price:.2f}")
#     else:
#         print("Invalid number of items!")
#
# if __name__ == "__main__":
#     main()
total_price = 0
num_items = int(input("items?: "))
while num_items <= 0:
    print("invalid")
    num_items = float(input("items?: "))
for i in range(num_items):
    total_price += float(input(f"enter price for item {i + 1}"))
if total_price >= 100:
    total_price *= DISCOUNT_RATE
print(f"total price for {num_items} items is ${total_price}")

