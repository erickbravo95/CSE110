
list_of_friends = []
friend_name = ""

while friend_name != "end":
    friend_name = input("Type the name of a friend:")
    if friend_name != "end":
        list_of_friends.append(friend_name)
         
print ("\nYour friends are:")
for friend in list_of_friends :
    print (friend)
