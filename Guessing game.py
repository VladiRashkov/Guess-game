import random
import sys
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
answer = random.randint(1, 100)
print(answer)
easy_guesses = 10
hard_guesses = 5


def easy(easy_guess, easy_guesses):
    if easy_guesses == 1:
        if answer == easy_guess:
            print("Correct guess")
            sys.exit()
        else:
            print("Game over")
            sys.exit()
    if answer == easy_guess:
        print("Correct guess")
        sys.exit()
    elif answer > easy_guess:
        easy_guesses -= 1
        print(f"You have {easy_guesses} attempts remaining to guess the number.\nToo low. \nGuess again.")
        return easy_guesses
    elif answer < easy_guess:
        easy_guesses -= 1
        print(f"You have {easy_guesses} attempts remaining to guess the number.\nToo high. \nGuess again.")
        return easy_guesses


def hard(hard_guess, hard_guesses):
    if hard_guesses == 1:
       if answer == hard_guess:
            print("Correct guess")
            sys.exit()     
       else:    
            print("Game over")
            sys.exit()

    if answer == hard_guess:
        print("Correct guess")
        sys.exit()
    elif answer > hard_guess:
        hard_guesses -= 1
        print(f"You have {hard_guesses} attempts remaining to guess the number.\nToo low. \nGuess again.")
        return hard_guesses
    elif answer < hard_guess:
        hard_guesses -= 1
        print(f"You have {hard_guesses} attempts remaining to guess the number.\nToo high. \nGuess again.")
        return hard_guesses


while True:
    if difficulty == "easy":
        easy_guess = int(input("Make a guess: "))
        easy_guesses = easy(easy_guess, easy_guesses)

    elif difficulty == "hard":
        hard_guess = int(input("Make a guess: "))
        hard_guesses = hard(hard_guess, hard_guesses)
