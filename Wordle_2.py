print ("Welcome to the word guessing game!")

secret_word = "dinosaur"
number_guesses = 0
guess = input("\nWhat is your guess? ")

while guess.lower() != secret_word:
   number_guesses = number_guesses + 1
   print("Your guess was not correct.")
   guess = input("What is your guess? ")

print ("Congratulations! You guessed it!")
print (f"It took you {number_guesses} guesses.")



