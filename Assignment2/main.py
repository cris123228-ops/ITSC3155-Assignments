import data
import sandwich_maker
import cashier


resources = data.resources
recipes = data.recipes

sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()


def display_report():
    print(f"Bread: {resources['bread']} slices")
    print(f"Ham: {resources['ham']} slices")
    print(f"Cheese: {resources['cheese']} ounces")


def main():
    machine_running = True

    while machine_running:
        choice = input(
            "What would you like? "
            "(small/medium/large/off/report): "
        ).lower().strip()

        if choice == "off":
            machine_running = False

        elif choice == "report":
            display_report()

        elif choice in recipes:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                print(f"The cost is ${cost:.2f}.")

                money_inserted = cashier_instance.process_coins()

                if cashier_instance.transaction_result(
                    money_inserted, cost
                ):
                    sandwich_maker_instance.make_sandwich(
                        choice, ingredients
                    )

        else:
            print(
                "Invalid selection. Please choose small, medium, "
                "large, report, or off."
            )


if __name__ == "__main__":
    main()