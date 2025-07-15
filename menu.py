# Restaurant Ordering System 

# This is the restaurant menu display.
menu = {
    "Burger": 250,
    "Pizza": 700,
    "Pasta": 420,
    "Fries": 350,
    "Coke": 130
}

# It will hold items and the quantity ordered by the customer.
order = {}

# Welcome message and displaying the menu to the customer.
print("Welcome to the Supreme Restaurant!")
print("Here's our menu:\n")

# Loop through the menu list and print each item with price.
for item, price in menu.items():
    print(f"{item}: Rs.{price}")

# Start a loop to take the customer's order.
while True:
    # Ask the customer what they want to order
    choice = input("\nWhat would you like to order? (type 'done' to finish): ").title()

    # If the user types 'done', we stop the ordering loop
    if choice == "Done":
        break

    # Check if the chosen item exists in the menu
    if choice in menu:
        # Ask how many units of the item the customer wants
        qty = int(input(f"How many {choice}s would you like? "))

        # If the item is already in the order, add the new quantity to it
        if choice in order:
            order[choice] += qty
        else:
            # If it's the first time the item is ordered, add it to the order dictionary
            order[choice] = qty

        # Confirm to the user that the item has been added
        print(f"{qty} {choice}(s) added to your order.")
    else:
        # If the item is not found in the menu
        print("Sorry, that item  is not available")

# Once ordering is done, we show the order summary
print("\n--- Order Summary ---")

# Initialize total bill to 0
total = 0

# Loop through each item in the order dictionary
for item, qty in order.items():
    # Get the price of the item from the menu
    price = menu[item]
    # Calculate total cost for that item
    item_total = price * qty
    # Print the item, quantity and total price for that item
    print(f"{item} x {qty} = Rs.{item_total}")
    # Add the item total to the final total
    total += item_total

# Print the final total bill
print(f"\nTotal bill: Rs.{total}")
print("Thank you for ordering with us! Enjoy your meal.")
