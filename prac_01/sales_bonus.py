"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        bonus = calculate_bonus(sales)
        print("Your Bonus is: ", round(bonus))
        sales = float(input("Enter sales: $"))


def calculate_bonus(sales):
    if sales < 1000:
        bonus = 0.1*sales
    else:
        bonus = 0.15*sales
    return bonus


main()
