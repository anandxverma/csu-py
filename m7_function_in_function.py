def print_receipt_store1(item_details: dict[str, float]):
    print("Store 1 receipt")
    print("*" * 30)
    total = 0
    for k, v in item_details.items():
        print(f"{k:<20} ${v:>5.2f}")
        total += v
    print("*" * 30)
    print(f"{'Total':<20} ${total:>5.2f}")

def print_receipt_store2(item_details: dict[str, float]):
    print("Store 2 receipt")
    print("=" * 30)
    total = 0
    amt_txt = ""
    for k, v in item_details.items():
        amt_txt = f"${v:.2f}".rjust(28 - len(k), "-")
        print(f"{k} {amt_txt}")
        total += v
    print("=" * 30)
    amt_txt = f"${total:.2f}".rjust(29 - len("Total"), "-")
    print(f"{'Total'} {amt_txt}")

def print_receipt(print_func, item_details: dict[str, float]):
    print_func(item_details)

# List of items
list_items = {
    "Aspirin": 10.50,
    "Ibuprofen": 5.00,
    "Antihistamines": 15.90,
    "Laxatives": 7.45
}

# Print receipts for Store 1
print("\n")
print_receipt(print_receipt_store1, list_items)
print("\n")

# Print receipts for Store 2
print_receipt(print_receipt_store2, list_items)
print("\n")