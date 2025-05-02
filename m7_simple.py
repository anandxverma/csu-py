def print_bill_item(item_label, item_amount):
    # Format the label and amount
    txt_to_print = item_label + item_amount.rjust(30 - len(item_label) - 1)
    txt_to_print += "\n" + "*" * 30
    print(txt_to_print)

# Ask the user to input the meal price
meal_price = float(input("\nEnter the price of the meal: $"))

# Calculate the tip amount @18%
tip = float(meal_price * 0.18)

# Calculate the tax amount @7%
tax = float(meal_price * 0.07)

# Calculate total cost
total_cost = meal_price + tip + tax

# Print the complete bill
print("\n")
print_bill_item("Meal price:", f"${meal_price:.2f}")
print_bill_item("Tip @18.00%", f"${tip:.2f}")
print_bill_item("Tax @7.00%", f"${tax:.2f}")
print_bill_item("Total cost:", f"${total_cost:.2f}")