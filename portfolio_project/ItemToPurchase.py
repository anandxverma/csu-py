# Class representing an item to purchase in a shopping cart
# Class has three attributes: item_name, item_price, and item_quantity
# Class has a two methods:
# A method to calculate the total cost of the item
# And a method to print the item details

class ItemToPurchase:

    # Constructor with default parameters
    def __init__(self, name: str = "none", price: float = 0.0, quantity: int = 0, description: str = "none"):
        self.__item_name = name
        self.__item_price = price
        self.__item_quantity = quantity
        self.__item_description = description

    # getter and setter for item_name
    @property
    def item_name(self):
        return self.__item_name
    @item_name.setter
    def item_name(self, name):
        self.__item_name = name

    # getter and setter for item_price
    @property
    def item_price(self):
        return self.__item_price
    @item_price.setter
    def item_price(self, price):
        if price >= 0:
            self.__item_price = price
        else:
            raise ValueError("Price cannot be negative.")
    
    # getter and setter for item_quantity
    @property
    def item_quantity(self):
        return self.__item_quantity
    @item_quantity.setter
    def item_quantity(self, quantity):
        if isinstance(quantity, int) and quantity >= 0:
            self.__item_quantity = quantity
        else:
            raise ValueError("Quantity is not a valid number.")

    # getter and setter for item_decription
    @property
    def description(self):
        return self.__item_description
    @description.setter
    def item_description(self, name):
        self.__item_description = name

    # Method to calculate total cost
    def calc_total_cost(self):
        return self.item_quantity * self.item_price

    # Method to return item details as string
    def __str__(self):
        return f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.calc_total_cost():.2f}"
    
    # Method to print item details
    def print_item_cost(self):
        print(self)
