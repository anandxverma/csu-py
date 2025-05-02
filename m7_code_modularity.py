def addItemToCart(itemName, itemPrice, itemQuantity):
    # TODO
    pass

def removeItemFromCart(itemName):
    # TODO
    pass

def calculateCartTotal():
    # TODO
    pass

def checkout():
    # TODO
    pass

# Main business logic of the Shopping Portal

# Initializing the shopping cart
list_items = [ {'name': 'apples', 'price': 0.49, 'quantity': 12}, {'name': 'oranges', 'price': 0.35, 'quantity': 6}, {'name': 'egg carton', 'price': 5.0, 'quantity': 2} ]

# Adding items to the cart
for item in list_items:
    addItemToCart(item['name'], item['price'], item['quantity'])

# Calculate cart total
calculateCartTotal()

# Check out the cart
checkout()