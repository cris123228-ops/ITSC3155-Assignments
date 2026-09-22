class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""

        large_dollars = int(input("How many large dollars?: "))
        half_dollars = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))

        total = (
            large_dollars * 1.00
            + half_dollars * 0.50
            + quarters * 0.25
            + nickels * 0.05
        )

        return round(total, 2)

    def transaction_result(self, coins, cost):
        """Returns True when payment is accepted or False if insufficient."""

        if coins >= cost:
            change = round(coins - cost, 2)

            if change > 0:
                print(f"Here is ${change:.2f} in change.")

            return True

        print("Sorry, that's not enough money. Money refunded.")
        return False