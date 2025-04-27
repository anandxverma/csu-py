import ShoppingCart as sc
import ItemToPurchase as itm
import datetime as dt
import time

def print_blinking_text(text, duration_sec, interval_sec=0.5):
    """Prints blinking text for a specified duration.
    Args:
        text: The text to blink.
        duration_sec: The total duration for blinking in seconds.
        interval_sec: The interval between blinks in seconds.
    """
    start_time = time.time()
    while time.time() - start_time < duration_sec:
        print(text, end="\r")  # Print text, carriage return to overwrite
        time.sleep(interval_sec)
        print(" " * len(text), end="\r")  # Print spaces to clear text
        time.sleep(interval_sec)

# Prints the menu of actions for the shopping cart
def print_menu(cart: sc.ShoppingCart):
    print("MENU:")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    return input("Choose an action: ").lower()

# Main function to run the shopping portal
# Initializes a shopping cart
print("\nWELCOME TO THE SHOPPING PORTAL")
customer_name = input("Please enter your name:").strip()
print("\nHello", customer_name, "! Your shopping cart is being initialized with some items...\n")
cart = sc.ShoppingCart(customer_name, dt.datetime.now().strftime("%B %d, %Y"))
print_blinking_text(" Adding Apples...", 1)
cart.add_item(itm.ItemToPurchase("Apple", 0.55, 6, "Fresh red apples"))
print_blinking_text(" Adding Bananas...", 1)
cart.add_item(itm.ItemToPurchase("Banana", 0.35, 12, "Ripe bananas"))
print_blinking_text(" Adding Oranges...", 1)
cart.add_item(itm.ItemToPurchase("Orange", 0.29, 5, "Juicy oranges"))
print_blinking_text(" Adding Grapes...", 1)
cart.add_item(itm.ItemToPurchase("Grapes", 2.99, 2, "Seedless grapes"))
print_blinking_text(" Adding Mangoes...", 1)
cart.add_item(itm.ItemToPurchase("Mango", 1.55, 4, "Sweet mangoes"))

# Print the shopping cart details
print("\nOUTPUT SHOPPING CART")
cart.print_cart()

# Print the menu of actions and prompt for user input
print()

action = print_menu(cart)
while action != "q":
    print()
    if action == "a":
        print("ADD ITEM TO CART")
        item_name = input("Enter the item name: ")
        item_price = float(input("Enter the item price: "))
        item_quantity = int(input("Enter the item quantity: "))
        item_description = input("Enter the item description: ")
        print()
        cart.add_item(itm.ItemToPurchase(item_name, item_price, item_quantity, item_description))
    elif action == "r":
        print("REMOVE ITEM FROM CART")
        item_name = input("Enter the item name to remove: ")
        print()
        cart.remove_item(item_name)
    elif action == "c":
        print("CHANGE ITEM QUANTITY")
        item_name = input("Enter the item name to modify: ")
        new_quantity = int(input("Enter the new quantity: "))
        print()
        cart.modify_item(itm.ItemToPurchase(item_name, None, new_quantity))
    elif action == "i":
        print("OUTPUT ITEMS' DESCRIPTIONS")
        cart.print_descriptions()
    elif action == "o":
        print("OUTPUT SHOPPING CART")
        cart.print_cart()
    else:
        print("Invalid action. Please choose a valid action from the MENU.")
        pass
    print()
    action = print_menu(cart)

print("\nExiting the shopping portal. Thank you!\n")