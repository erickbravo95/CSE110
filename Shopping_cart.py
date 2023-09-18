items_list = []
prices_list = []
enter_action = None
print ("Welcome to the Shopping Cart Program!")

while enter_action != 5:
    print ("\nPlease select one of the following:")
    print ("1. Add item")
    print ("2. View cart")
    print ("3. Remove item")
    print ("4. Compute total")
    print ("5. Quit")
    enter_action = int(input("Please enter an action: "))
    
    if enter_action == 1:
        item_added = input("What item would you like to add? ")
        price_item = int(input(f"What is the price of '{item_added}'? "))
        items_list.append (item_added)
        prices_list.append (price_item)
        print(f"'{item_added}' has been added to the cart.")
    
    if enter_action == 2:
        print ("The contents of the shopping cart are:")
        for i in range(len(items_list)):
             print(f"{i+1}. {items_list[i]} - ${prices_list[i]}")

    if enter_action == 3:
        remove_item = int(input("Which item would you like to remove? "))
        if remove_item > len(items_list):
            print("Sorry, that is not a valid item number.")
        else:
            items_list.pop (remove_item-1)
            prices_list.pop (remove_item-1)
            print ("Item removed.")
                
    if enter_action == 4:
        total_cart = sum(prices_list)
        print (f"The total price of the items in the shopping cart is ${total_cart:.2f}")
            
        
print("Thank you. Goodbye.")
