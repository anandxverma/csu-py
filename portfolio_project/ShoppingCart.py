import ItemToPurchase as itm

class ShoppingCart:
    """Class to represent an online shopping cart."""

    # Class constructor
    def __init__(self, customer_name: str = "none", current_date: str = "January 1, 2020"):
        # Initialize the shopping cart with customer name, date, and an empty list of items
        self.__customer_name = customer_name
        self.__current_date = current_date
        self.__cart_items = []

    # Method check if an item is already in the cart
    def find_item(self, item_name: str) -> itm.ItemToPurchase:
        # Iterate through the cart items to check if the item is already in the cart
        for item in self.__cart_items:
            if item.item_name.lower() == item_name.lower():
                return item
        return None

    # Method to add an item to the shopping cart
    def add_item(self, item: itm.ItemToPurchase):
        # Check if the item is already in the cart
        existing_item = self.find_item(item.item_name)
        # If the item is already in the cart, update its quantity
        if existing_item:
            existing_item.item_quantity += item.item_quantity
            print(f"Item '{item.item_name}' already in cart. Quantity updated to {existing_item.item_quantity}.")
        else:
            self.__cart_items.append(item)
            print(f"Item '{item.item_name}' added to the cart.")

    # Method to remove an item from the shopping cart by name
    def remove_item(self, item_name: str):
        # Default action taken message
        action_taken = f"Item '{item_name}' not found in the cart. Nothing removed."
        # Check if the item is in the cart
        existing_item = self.find_item(item_name)
        # If the item is in the cart, remove it
        if existing_item is not None:
            # Remove the item from the cart
            self.__cart_items.remove(existing_item)
            action_taken = f"Item '{item_name}' removed from the cart."

        # Print the action taken
        print(action_taken)

    # Method to modify an existing item in the shopping cart
    def modify_item(self, item_to_mod: itm.ItemToPurchase):
        # Iterate through the cart items to find the item to modify
        item_mod_name = item_to_mod.item_name
        # Initialize the action taken message to default
        action_taken = f"Item '{item_mod_name}' not found in the cart. Nothing removed."
        # Check if the item is in the cart
        existing_item = self.find_item(item_mod_name)

        # If the item is in the cart, update its price and quantity
        # If the item price is not specified, keep the existing price
        # If the item quantity is not specified, keep the existing quantity
        if existing_item is not None:
            existing_item.item_price = existing_item.item_price if item_to_mod.item_price is None else item_to_mod.item_price
            existing_item.item_quantity = existing_item.item_quantity if item_to_mod.item_quantity is None else item_to_mod.item_quantity
            action_taken = f"Item '{item_mod_name}' updated."

        # Print the action taken
        print(action_taken)

    # Get the number of items in the shopping cart
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.__cart_items)
    
    # Get the total cost of all items in the shopping cart
    def get_cost_of_cart(self):
        total_cost = 0
        # Iterate through the cart items to calculate the total cost
        for item in self.__cart_items:
            total_cost += item.calc_total_cost()
        return total_cost
    
    # Shopping cart details as string
    def __str__(self):
        # Cart header
        txt = f"{self.__customer_name}'s Shopping Cart - {self.__current_date}"
        # Cart items
        if self.get_num_items_in_cart() == 0:
            txt += "\nShopping cart is empty"
        else:
            txt += f"\nNumber of Items: {self.get_num_items_in_cart()}"
            for item in self.__cart_items:
                txt += f"\n{item}"
        # Total cost
        txt += f"\nTotal: ${self.get_cost_of_cart():.2f}"
        # Return the final string representation of the shopping cart
        return txt        

    # Print the total cost of the shopping cart
    def print_total(self):
        if self.get_num_items_in_cart() == 0:
            print("Shopping cart is empty")
        else:
            print("Total: $", f"{self.get_cost_of_cart():.2f}")

    # Print the shopping cart details
    def print_cart(self):
        print(self)

    # Print shopping cart with item descriptions
    def print_descriptions(self):
        print(f"{self.__customer_name}'s Shopping Cart - {self.__current_date}")
        print("Item Descriptions")
        for item in self.__cart_items:
            print("{}: {}".format(item.item_name, item.item_description))
 