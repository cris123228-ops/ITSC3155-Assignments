
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if insufficient."""

        for item, amount_needed in ingredients.items():
            if self.machine_resources[item] < amount_needed:
                print(f"Sorry, there is not enough {item}.")
                return False

        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deducts ingredients and makes the sandwich."""

        for item, amount_needed in order_ingredients.items():
            self.machine_resources[item] -= amount_needed

        print(f"Your {sandwich_size} sandwich is ready. Bon appetit!")