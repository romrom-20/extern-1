# Inventory Management Program
# Author: saman

def display_inventory(inventory):
    print("Current inventory:")
    for item, (quantity, price) in inventory.items():
        print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")

def calculate_total_value(inventory):
    total = sum(quantity * price for quantity, price in inventory.values())
    print(f"Total value of inventory: ${total}")

def main():
    print("Welcome to the Inventory Manager!")
    inventory = {
        "apple": (10, 2.5),
        "banana": (20, 1.2)
    }
    display_inventory(inventory)

    # Add a new item
    print("Adding a new item: mango")
    inventory["mango"] = (15, 3.0)
    print("Updated inventory:")
    display_inventory(inventory)

    calculate_total_value(inventory)

if __name__ == "__main__":
    main()
