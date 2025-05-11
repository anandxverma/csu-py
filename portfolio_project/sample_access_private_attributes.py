import ItemToPurchase as item

i1 = item.ItemToPurchase(name="Chocolate Bar", price=1.50, quantity=5, description="Dark chocolate bar")

print(i1._ItemToPurchase__item_name)  # Accessing private variable directly (not recommended)