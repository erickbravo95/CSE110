child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
child_num = int(input("How many children are there? "))
adult_num = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

total_child = child_meal * child_num
total_adult = adult_meal * adult_num
subtotal = total_adult + total_child
sale_tax = (subtotal * tax_rate) / 100
total = subtotal + sale_tax

print (f"\nSubtotal: ${subtotal}")
print (f"Sales Tax: ${sale_tax:.2f}")
print (f"Total: ${total:.2f}")

payment = float(input("\nWhat is the payment amount? "))

change = payment - total

print (f"Change: ${change:.2f}")

payment = input("\nWould you like to leave a tip?(Y/N) ")

if payment == "Y":
    tip = float(input("How much money would you like to leave? "))
    waiters_pocket = tip
    print ("\nThank you! Come back soon!")
else:
    print ("\nThank you! Come back soon!")
