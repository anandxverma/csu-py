import ItemToPurchase as itm

# Ask the user to enter details for all purchased items
# Minimum 2 and Maximum 5 items are allowed
MIN_ITEMS = 2
MAX_ITEMS = 5
# Initialize an empty list to store item instances
items = []
item_count = 0
while True:
    try:
        print()        
        # Ask the user to enter item details
        print("Add item",  item_count + 1, "to the cart")
        item_name = input("Enter the item name: ")
        item_price = float(input("Enter the item price: $"))
        item_quantity = int(input("Enter the item quantity: "))

        # Set item details and add to the items list
        item = itm.ItemToPurchase(item_name, item_price, item_quantity)
        items.append(item)
        print(item, "added to the cart.")

        # Increment item count to record the number of items in the list
        item_count += 1

        # Check if the number of items is within the allowed range
        if item_count < MIN_ITEMS:
            continue
        elif item_count == MIN_ITEMS:
            # Ask if the user wants to add another item
            print()
            print("You have added the minimum needed", item_count, "items.")
            another_item = input("Do you want to add more items? (y/n): ").strip().lower() or 'y'
            if another_item != 'y':
                break
        elif item_count > MIN_ITEMS and item_count < MAX_ITEMS:
            # Ask if the user wants to add another item
            print()
            print("You have", item_count, "items in the cart.")
            another_item = input("Do you want to add more items? (y/n): ").strip().lower() or 'y'
            if another_item != 'y':
                break
        else:
            print()
            print("You have reached the maximum allowed", MAX_ITEMS, "items in the cart.")
            break
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")
        break

# Calculate and print the total cost of all items
total_cost = sum(item.calc_total_cost() for item in items)
print()
print("\nTOTAL COST")
for item in items:
    item.print_item_cost()
print("-" * 30)
print(f"Total: ${total_cost:.2f}")
