first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

tuki = f'Your name is {last_name}, {first_name} {last_name}.'
print(tuki)

#otras funciones 
#tuki = f'Your name is {last_name.upper}, {first_name.lower} {last_name.capitalize} {first_name.count("a")}.'
#print(tuki)

#formas menos efectivas
#tuki = "Your name is " + last_name + ", " + first_name + last_name + "."
#tuki = "Your name is {}, {} {}".format(last_name,first_name,last_name)
#tuki = "Your name is {1}, {0} {1}".format(first_name,last_name)
#print(tuki)

