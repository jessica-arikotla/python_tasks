#1. Add Product
inventory = {}
def add_product():
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    category = input("Enter category: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter price: "))
    inventory[pid] = {
        "name": category,
        "category": category,
        "qty": qty,
        "price": price

    }
    print("Product Added Successfully!")

#2. Update Inventory
def update_inventory():
    pid = input("Enter Product ID: ")
    if pid in inventory:
        inventory[pid]["qty"] = int(input("Enter New Quantity: "))
        inventory[pid]["price"] = float(input("Enter New Price: "))
        print("product Updated Successfully!")
    else:
        print("Product Not Found!")

#3. Search Product
def search_product():
    pid = input("Enter Product ID: ")
    if pid in inventory:
        print(inventory[pid])
    else:
        print("Product Not found!")

#4. Display Inventory
def display_inventory():
    for pid, details in inventory.items():
        print("\nProduct ID:", pid)
        print("Name:", details["name"])
        print("Category:", details["category"])
        print("Quantity:", details["qty"])
        print("Price:", details["price"])

#5.Low stock Alert
def low_stock_alert():
    print("\nLow Stock Product")
    for pid, details in inventory.items():
        if details["qty"] < 10:
            print(details["name"])

#6. Out of Stock Alert
def out_of_stock_alert():
    print("\nout of Stock Products")
    for pid, details in inventory.items():
        if detail["qty"] == 0:
            print(details["name"])

#7. Category Management
def Category_Management():
    categories = set()
    for details in inventory.values():
        categories.add(details["category"])
    print("Available Categories:")
    for category in categories:
        print(category)

#8. Inventory Report
def inventory_report():
    total_items = 0
    total_value = 0

    for details in inventory.values():
        total_items += details["qty"]
        total_value += details["qty"] * details["Price"]
        print("Total Items:", total_items)
        print("Total Value:", total_value)

#9.Delete Product
        def delete_product():
            pid = input("Enter Product ID: ")
            if pid in inventory:
                del inventory[pid]
                print("Product Deleted Successfully!")
            else:
                print("Product Not found!")

while True:
 print("\n1. Add Product")
 print("2. Display Inventory")
 print("3. Exit")
 choice = input("Enter choice: ")

 if choice == "1":
    add_product()
 elif choice == "2":
    display_inventory()
 elif choice == "3":
    break
        








































    
