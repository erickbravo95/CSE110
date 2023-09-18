color = input('Please type your favorite color: ')
if color == "black":
    print ("\033[1;30;40m"+color,"... That's a great color! I like it.")
elif color == "red":
    print ("\033[1;31;40m"+color,"... That's a great color! I like it.")
elif color == "green":
    print ("\033[1;32;40m"+color,"... That's a great color! I like it.")
elif color == "yellow":
    print ("\033[1;33;40m"+color,"... That's a great color! I like it.")
elif color == "blue":
    print ("\033[1;34;40m"+color,"... That's a great color! I like it.")
elif color == "purple":
    print ("\033[1;35;40m"+color,"... That's a great color! I like it.")
elif color == "cyan":
    print ("\033[1;36;40m"+color,"... That's the best color! I love it.")
elif color == "white":
    print ("\033[1;37;40m"+color,"... That's a great color! I like it.")
else:
    print (color,"... That is a great color! I like it.")

