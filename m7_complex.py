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
# Print meal price
print("Meal price:" + " "*10 + f"${meal_price:.2f}")
print("*" * 28)
# Print tip
print("Tip @18.00%" + " " *11 + f"${tip:.2f}")
print("*" * 28)
# Print tax
print("Tax @7.00%" + " " *12 + f"${tax:.2f}")
print("*" * 28)
# Print total cost
print("Total cost:" + " "*10 + f"${total_cost:.2f}")
print("*" * 28)