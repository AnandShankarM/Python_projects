#Guessing numbers
import random
def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 to 100")

    num = random.randint(1, 100)
    difficulty_level = input("Choose a difficulty level? Easy or Hard \n").lower()
    if difficulty_level == 'easy':
        attempts = 10
    elif difficulty_level == 'hard':
        attempts = 5
    else:
        print("Please type easy or hard")
        return

    print(f"You have {attempts} attempts remaining to guess the number")
    while attempts > 0:
        guessed_number = int(input("Make a guess \n"))
        if guessed_number < 1 or guessed_number > 100:
            print("Please guess the number between 1 to 100")
            attempts -= 1
            continue
        elif guessed_number == num:
            print(f"You've got it!. The answer is {guessed_number}")
            return
        elif guessed_number > num:
            print("Its too high")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number \n")
        elif guessed_number < num:
            print("Its too low")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number \n")

    if attempts == 0:
        print("You loose")

game()
