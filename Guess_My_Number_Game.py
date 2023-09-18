import random

number = random.randint(1 , 100)
guess = int(input("What is your guess? "))
while guess < number :
    print("Oops! You need to guess higher.")
    guess = int(input("What is your guess? "))
while guess > number :
    print("Oops! You need to guess lower.")
    guess = int(input("What is your guess? "))
print("Congratulations! You guessed it correctly")

repeat = input("Do you want to play again? ")
while repeat.lower() == "yes" :
    guess = int(input("What is your guess? "))
    while guess < number :
        print("Oops! You need to guess higher.")
        guess = int(input("What is your guess? "))
    while guess > number :
        print("Oops! You need to guess lower.")
        guess = int(input("What is your guess? "))
    print("Congratulations! You guessed it correctly")
    repeat = input("Do you want to play again? ")
print("Thanks for playing!")