# 1. Set up order list at the beginning of the file
order = []  # This will store the customer's order

# Rest of the original code remains the same until the menu item selection part
# After printing the menu items and before asking for customer input:

# 2. Get customer's menu selection
menu_selection = input("What would you like to order? Enter menu item number: ")

# 3. Check if the input is a number
if menu_selection.isdigit():
    # Convert to integer
    menu_selection = int(menu_selection)
    
    # 4. Check if the selection is valid and process the order
    if menu_selection in menu_items.keys():
        # Get the item name
        item_name = menu_items[menu_selection]["Item name"]
        
        # Ask for quantity
        quantity = input(f"How many {item_name} would you like? (Default is 1): ")
        
        # Validate quantity input
        if quantity.isdigit():
            quantity = int(quantity)
        else:
            quantity = 1
            
        # Add item to order
        order.append({
            "Item name": item_name,
            "Price": menu_items[menu_selection]["Price"],
            "Quantity": quantity
        })
        print(f"{quantity} {item_name}(s) added to your order.")
    else:
        print("Invalid menu selection.")
else:
    print("Invalid input. Please enter a number.")

# 5. Replace the while True loop for keeping order with:
while True:
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()
    
    match keep_ordering:
        case 'y':
            place_order = True
            break
        case 'n':
            place_order = False
            print("Thank you for your order!")
            break
        case _:
            print("Invalid input. Please enter 'Y' or 'N'.")

# After the ordering loop ends, print the receipt:

print("\nThis is what we are preparing for you.\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6-10. Print the receipt
for item in order:
    # Store variables
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]
    
    # Calculate spaces for formatting
    name_spaces = " " * (24 - len(item_name))
    price_spaces = " " * (6 - len(str(price)))
    
    # Print formatted line
    print(f"{item_name}{name_spaces} | ${price}{price_spaces} | {quantity}")

# 11. Calculate and print total
total = sum(item["Price"] * item["Quantity"] for item in order)
print("\nTotal: ${:.2f}".format(total))
