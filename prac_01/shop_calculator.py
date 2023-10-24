"""
A shop requires a small program that would allow them to quickly work out the total price for a number of items, each with different prices.

The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
"""

num_item = int(input("Number of items: "))
total_price = 0

while num_item < 0:
    print(f"Invalid number of items!")
    num_item = int(input("Number of items: "))

for i in range(1, num_item+1):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {num_item} items is ${total_price:.2f}")


