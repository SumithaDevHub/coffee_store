class CoffeeMachine:
    def __init__(self):
        self.water = 1000  # in milliliters
        self.milk = 1000  # in milliliters
        self.coffee_beans = 200  # in grams
        self.filter_coffee_powder = 100  # in grams, specific for filter coffee
        self.money = 0  # in INR

    def check_resources(self, water_needed, milk_needed, coffee_needed, filter_coffee_needed=0):
        if self.water < water_needed:
            print("Sorry, not enough water!")
            return False
        if self.milk < milk_needed:
            print("Sorry, not enough milk!")
            return False
        if coffee_needed and self.coffee_beans < coffee_needed:
            print("Sorry, not enough coffee beans!")
            return False
        if filter_coffee_needed and self.filter_coffee_powder < filter_coffee_needed:
            print("Sorry, not enough filter coffee powder!")
            return False
        return True

    def process_payment(self, cost):
        print(f"The cost is ₹{cost}")
        payment = float(input("Please enter the payment amount: ₹"))
        if payment < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        elif payment > cost:
            print(f"Here is ₹{round(payment - cost, 2)} in change.")
        self.money += cost
        return True

    def make_coffee(self, water_needed, milk_needed, coffee_needed, filter_coffee_needed=0):
        self.water -= water_needed
        self.milk -= milk_needed
        if coffee_needed:
            self.coffee_beans -= coffee_needed
        if filter_coffee_needed:
            self.filter_coffee_powder -= filter_coffee_needed
        print("Here is your coffee ☕️. Enjoy!")

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee Beans: {self.coffee_beans}g")
        print(f"Filter Coffee Powder: {self.filter_coffee_powder}g")
        print(f"Money: ₹{self.money}")

    def start(self):
        while True:
            choice = input("What would you like? (espresso/latte/cappuccino/filter coffee/report/off): ").lower()
            if choice == "off":
                print("Turning off the coffee machine. Goodbye!")
                break
            elif choice == "report":
                self.report()
            elif choice in ["espresso", "latte", "cappuccino", "filter coffee"]:
                if choice == "espresso":
                    water_needed, milk_needed, coffee_needed, filter_coffee_needed, cost = 50, 0, 18, 0, 50
                elif choice == "latte":
                    water_needed, milk_needed, coffee_needed, filter_coffee_needed, cost = 200, 150, 24, 0, 100
                elif choice == "cappuccino":
                    water_needed, milk_needed, coffee_needed, filter_coffee_needed, cost = 250, 100, 24, 0, 120
                elif choice == "filter coffee":
                    water_needed, milk_needed, coffee_needed, filter_coffee_needed, cost = 100, 200, 0, 20, 80
                if self.check_resources(water_needed, milk_needed, coffee_needed, filter_coffee_needed):
                    if self.process_payment(cost):
                        self.make_coffee(water_needed, milk_needed, coffee_needed, filter_coffee_needed)
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.start()
