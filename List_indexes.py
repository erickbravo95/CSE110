
items_list = []
enter_item = None

print ("Please enter the items of the shopping list (type: quit to finish):")
while enter_item != "quit": 
    enter_item = input("Item: ")
    if enter_item != "quit":
        items_list.append(enter_item)

print ("\nThe shopping list is:")
for items in items_list:
    print(items)

print ("\nThe shopping list with indexes is:")
for i in range(len(items_list)):
    present_items = items_list[i]
    print(f"{i}. {present_items}")

change_item = int(input("\nWhich item would you like to change? "))
new_item = input("What is the new item?")
items_list.pop(change_item)
items_list.insert(change_item,new_item)

print ("\nThe shopping list with indexes is:")
for j in range(len(items_list)):
    present_items = items_list[j]
    print(f"{j}. {present_items}")