# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("~" * 50)
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    main_menu = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        main_menu[i] = key
        # Add 1 to the menu item number
        i += 1
    print("~" * 50)
    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in main_menu.keys():
            # Save the menu category name to a variable
            menu_category_name = main_menu[int(menu_category)]
            # Print out the menu category name they selected

            print(f"\nYou selected {menu_category_name}")
            print("*" * 50)
            # Print out the menu options from the menu_category_name
            print(f"\nWhat {menu_category_name} item would you like to order?\n")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            print("-------|--------------------------|-------")
            # 2. Ask customer to input menu item number
            #print(f"MenuItems Dictionary: {menu_items}")
            sel_menu_item = input(f"Type item number: ")

            # 3. Check if the customer typed a number
            if sel_menu_item.isdigit():
                # Convert the menu selection to an integer
                item_num = int(sel_menu_item)

                # 4. Check if the menu selection is in the menu items
                if item_num in menu_items.keys():
                    # Store the item name as a variable
                    s_item_name = menu_items[item_num]['Item name']

                    # Ask the customer for the quantity of the menu item
                    sel_item_qty = input(f"\nYou selected {s_item_name}, type item quantity: ")

                    # Check if the quantity is a number, default to 1 if not
                    if sel_item_qty.isdigit(): 
                        s_item_qty = int(sel_item_qty)
                    else:
                        s_item_qty = 1

                    # Add the item name, price, and quantity to the order list
                    order_list.append({'item_name': s_item_name, 'item_qty': s_item_qty, 'item_price': menu_items[item_num]['Price']})
                else:
                    # Tell the customer that their input isn't valid
                    print(f"ERROR: Your input is not in menu.")
            else:
                # Tell the customer they didn't select a menu option
                print(f"ERROR: You typed invalid character, type item number.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"ERROR: {menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("ERROR: You didn't select a number.")

    order_complete = False
    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("\n Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        match keep_ordering.lower():
                # Keep ordering, break this loop and display main menu
                # to continue
                case 'y':
                    break
                case 'n':
                    # Complete the order                    
                    # Since the customer decided to stop ordering, thank them for
                    # their order
                    # Exit the keep ordering question loop
                    order_complete = True
                    print(f"\n****Thank you for your order.****")
                    break
                case _:
                    # Tell the customer to try again
                    print(f"ERROR: Invalid selection. Type Y or N to continue.")
                    
    if order_complete:
        place_order = False

if place_order == False:
    # Print out the customer's order
    print("\n This is what we are preparing for you.\n")

    # Uncomment the following line to check the structure of the order
    #print(order_list)

    print(f"{'Item name':^26}|{'Price':^8}|{'Quantity':^10}|{'Total':^10}")
    print("--------------------------|--------|----------|---------")

    # 6. Loop through the items in the customer's order
    for eachOrderItem in order_list:
        # since we know already all the items in list are of type dict
        # we dont have to check for type in this case
        # 7. Store the dictionary items as variables
        oItemName = eachOrderItem['item_name']
        oItemPrice = eachOrderItem['item_price']
        oItemQty = eachOrderItem['item_qty']
        oItemTotal = (eachOrderItem['item_price'] * eachOrderItem['item_qty'])
        
        # 8. Calculate the number of spaces for formatted printing
        # 9. Create space strings
        #oname_space = " " * (24 - len(oItemName))    
        #oqty_space = " " * (8 - len(str(oItemQty)))
                            
        # 10. Print the item name, price, and quantity
        # using f string alignment instead of space
        print(f" {oItemName:<25}| {oItemPrice}   | {oItemQty:>8} | {oItemTotal:>8.2f}")

    print("--------------------------------------------------------")

    # 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.

order_total = sum([ (eachOrder['item_price'] * eachOrder['item_qty']) for eachOrder in order_list ])

sTotal = " " * (68 - len("Total: {order_total:.2f}"))
print(f"{sTotal}\033[1mTotal: {order_total:.2f}\033[0m")

#print(f"\033[1mTotal: {order_total:>49.2f}\033[0m")
print("--------------------------------------------------------")