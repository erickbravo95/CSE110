bank_list = []
balance_list = []
acount_name = ""

print ("Enter the names and balances of bank accounts (type: quit when done)")
while acount_name != "quit":
    acount_name = input("What is the name of this account? ")
    if acount_name != "quit":
        bank_list.append(acount_name)
        balance = int(input("What is the balance? "))
        balance_list.append(balance)

print("Account Information:")
for i in range(len(bank_list)):
    print (f"{bank_list[i]} - ${balance_list[i]}")

total = sum(balance_list)
ave = total / len(balance_list)
print (f"Total: ${total:.2f}")
print (f"Average: ${ave:.2f}")