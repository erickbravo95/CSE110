
def display_regular(thing):
    print(thing)

def display_uppercase(thing):
    upper_thing = thing.upper()
    print(upper_thing)

def display_lowercase(thing):
    lower_thing = thing.lower()
    print(lower_thing)

message = input("What is your message? ")

display_regular(message)
display_uppercase(message)
display_lowercase(message)
