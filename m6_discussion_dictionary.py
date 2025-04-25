class Contacts:

    # Class properties
    name = ""
    phone = ""
    address = ""

    def __init__(self, name: str = "", phone: str = "", address: str = ""):
        self.name = name
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, phone: {self.phone}, address: {self.address}"

def print_contacts(contacts):
    print("Contacts List:")
    print("*" * 20)
    for k in contacts:
        print(str(contacts[k]))
    print("*" * 20)
    print()

# Contacts List
contacts = { "john doe": Contacts("John Doe", "123-456-7890", "123 Elm St"),
            "jane smith":  Contacts("Jane Smith", "987-654-3210", "456 Oak St"),
            "alice johnson":  Contacts("Alice Johnson", "555-123-4567", "789 Pine St"),
            "bob brown": Contacts("Bob Brown", "444-555-6666", "321 Maple St")
}
# Print contacts
print_contacts(contacts)

print("Would you like to add or update a contact?")
add_or_update = int(input("Choose 1 to add, 2 to update, 3 to delete, or 0 to skip: "))
print()
if add_or_update == 1:
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number of the contact: ")
    address = input("Enter the address of the contact: ")
    contacts[name] = Contacts(name, phone, address)
    print()
    print("Contacts list updated successfully...")
    print_contacts(contacts)
elif add_or_update == 2:
    name = input("Enter the name of the contact to update: ").lower()
    if name in contacts:
        phone = input("Enter the new phone number of the contact: ")
        address = input("Enter the new address of the contact: ")
        contacts[name].phone = phone
        contacts[name].address = address
        print()
        print("Contacts list updated successfully...")
        print_contacts(contacts)
    else:
        print()
        print(f"Contact {name} not found.")
elif add_or_update == 3:
    name = input("Enter the name of the contact to delete: ").lower()
    if name in contacts:
        del contacts[name]
        print()
        print("Contact deleted successfully...")
        print_contacts(contacts)
    else:
        print()
        print(f"Contact {name} not found.")
else:
    print()
    print("No changes made to the contacts list.")