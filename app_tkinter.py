import tkinter as tk
from tkinter import messagebox

class CoffeeMachine:
    def __init__(self):
        self.water = 1000  # in milliliters
        self.milk = 1000  # in milliliters
        self.coffee_beans = 200  # in grams
        self.filter_coffee_powder = 100  # in grams, specific for filter coffee
        self.money = 0  # in INR
        self.current_cost = 0  # To store the cost of the selected coffee

    def check_resources(self, water_needed, milk_needed, coffee_needed, filter_coffee_needed=0):
        if self.water < water_needed:
            messagebox.showerror("Error", "Sorry, not enough water!")
            return False
        if self.milk < milk_needed:
            messagebox.showerror("Error", "Sorry, not enough milk!")
            return False
        if coffee_needed and self.coffee_beans < coffee_needed:
            messagebox.showerror("Error", "Sorry, not enough coffee beans!")
            return False
        if filter_coffee_needed and self.filter_coffee_powder < filter_coffee_needed:
            messagebox.showerror("Error", "Sorry, not enough filter coffee powder!")
            return False
        return True

    def process_payment(self):
        try:
            payment = float(payment_entry.get())
            if payment < self.current_cost:
                messagebox.showerror("Error", "Sorry, that's not enough money. Money refunded.")
                return False
            elif payment > self.current_cost:
                change = round(payment - self.current_cost, 2)
                change_label.config(text=f"Here is ₹{change} in change.")
            else:
                change_label.config(text="Exact amount received. No change.")
            self.money += self.current_cost
            return True
        except ValueError:
            messagebox.showerror("Error", "Invalid payment amount entered.")
            return False

    def make_coffee(self, water_needed, milk_needed, coffee_needed, filter_coffee_needed=0):
        self.water -= water_needed
        self.milk -= milk_needed
        if coffee_needed:
            self.coffee_beans -= coffee_needed
        if filter_coffee_needed:
            self.filter_coffee_powder -= filter_coffee_needed
        messagebox.showinfo("Enjoy", "Here is your coffee ☕️. Enjoy!")

    def report(self):
        report_text.set(
            f"Water: {self.water}ml\n"
            f"Milk: {self.milk}ml\n"
            f"Coffee Beans: {self.coffee_beans}g\n"
            f"Filter Coffee Powder: {self.filter_coffee_powder}g\n"
            f"Money: ₹{self.money}"
        )

def on_coffee_selected(choice):
    global water_needed, milk_needed, coffee_needed, filter_coffee_needed
    if choice == "espresso":
        water_needed, milk_needed, coffee_needed, filter_coffee_needed, cost = 50, 0, 18, 0, 50
    elif choice == "latte":
        water_needed, milk_needed, coffee_needed, filter_coffee_needed, cost = 200, 150, 24, 0, 100
    elif choice == "cappuccino":
        water_needed, milk_needed, coffee_needed, filter_coffee_needed, cost = 250, 100, 24, 0, 120
    elif choice == "filter coffee":
        water_needed, milk_needed, coffee_needed, filter_coffee_needed, cost = 100, 200, 0, 20, 80

    if machine.check_resources(water_needed, milk_needed, coffee_needed, filter_coffee_needed):
        machine.current_cost = cost
        cost_label.config(text=f"The cost is ₹{cost}.")
        make_coffee_button.config(state=tk.NORMAL)
        payment_entry.config(state=tk.NORMAL)
        payment_entry.delete(0, tk.END)
        change_label.config(text="")

def make_coffee_action():
    if machine.process_payment():
        machine.make_coffee(water_needed, milk_needed, coffee_needed, filter_coffee_needed)
        update_report()

def update_report():
    machine.report()

if __name__ == "__main__":
    machine = CoffeeMachine()

    # Create the main window
    root = tk.Tk()
    root.title("Coffee Machine")
    
    # Maximize the window to full screen
    root.attributes('-fullscreen', True)
    
    # Optional: Hide the window decorations
    root.overrideredirect(True)

    # Add a label to display the report
    report_text = tk.StringVar()
    report_label = tk.Label(root, textvariable=report_text, justify="left", font=("Arial", 12), bg="#F7F6F2", padx=20, pady=20)
    report_label.pack(pady=20, expand=True)

    # Frame for coffee selection
    coffee_frame = tk.Frame(root, bg="#F7F6F2")
    coffee_frame.pack(expand=True)

    # Buttons for selecting coffee
    tk.Button(coffee_frame, text="Espresso", command=lambda: on_coffee_selected("espresso"), width=20, pady=10).grid(row=0, column=0, padx=20, pady=10)
    tk.Button(coffee_frame, text="Latte", command=lambda: on_coffee_selected("latte"), width=20, pady=10).grid(row=0, column=1, padx=20, pady=10)
    tk.Button(coffee_frame, text="Cappuccino", command=lambda: on_coffee_selected("cappuccino"), width=20, pady=10).grid(row=0, column=2, padx=20, pady=10)
    tk.Button(coffee_frame, text="Filter Coffee", command=lambda: on_coffee_selected("filter coffee"), width=20, pady=10).grid(row=1, column=1, padx=20, pady=10)

    # Display the cost
    cost_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#F7F6F2")
    cost_label.pack(pady=10)

    # Entry for payment
    payment_frame = tk.Frame(root, bg="#F7F6F2")
    payment_frame.pack(pady=10)

    tk.Label(payment_frame, text="Enter payment (₹):", font=("Arial", 14), bg="#F7F6F2").grid(row=0, column=0, padx=10)
    payment_entry = tk.Entry(payment_frame, state=tk.DISABLED, font=("Arial", 14))
    payment_entry.grid(row=0, column=1, padx=10)

    # Button to make coffee
    make_coffee_button = tk.Button(payment_frame, text="Make Coffee", command=make_coffee_action, state=tk.DISABLED, font=("Arial", 14))
    make_coffee_button.grid(row=0, column=2, padx=10)

    # Label to show change
    change_label = tk.Label(root, text="", font=("Arial", 14, "italic"), bg="#F7F6F2")
    change_label.pack(pady=10)

    # Button to update report
    tk.Button(root, text="Show Report", command=update_report, width=20, font=("Arial", 14)).pack(pady=10)

    # Button to turn off the machine
    tk.Button(root, text="Turn Off", command=root.quit, width=20, font=("Arial", 14)).pack(pady=10)

    # Initialize the report display
    update_report()

    root.mainloop()
