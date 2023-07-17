import random
import sys

print('''  _____            _   _ _____   ____  __  __       _   _ _    _ __  __ ____  ______ _____             _____ _    _ ______  _____ _____ ______ _____     
 |  __ \     /\   | \ | |  __ \ / __ \|  \/  |     | \ | | |  | |  \/  |  _ \|  ____|  __ \           / ____| |  | |  ____|/ ____/ ____|  ____|  __ \    
 | |__) |   /  \  |  \| | |  | | |  | | \  / |     |  \| | |  | | \  / | |_) | |__  | |__) |         | |  __| |  | | |__  | (___| (___ | |__  | |__) |   
 |  _  /   / /\ \ | . ` | |  | | |  | | |\/| |     | . ` | |  | | |\/| |  _ <|  __| |  _  /          | | |_ | |  | |  __|  \___ \\___ \|  __| |  _  /    
 | | \ \  / ____ \| |\  | |__| | |__| | |  | |     | |\  | |__| | |  | | |_) | |____| | \ \          | |__| | |__| | |____ ____) |___) | |____| | \ \    
 |_|  \_\/_/    \_\_| \_|_____/ \____/|_|  |_|     |_| \_|\____/|_|  |_|____/|______|_|  \_\          \_____|\____/|______|_____/_____/|______|_|  \_\   

                                                                                                                                                         ''')
print("Welcome to random number guesser, guess the number  from 1-100\n")


def play_again():
    play = input("Do You Want to play again? Y/N")
    if play.upper() == "Y":
        return True
    else:
        return False


def attempt_checker():
    diff = int(input("CHOOSE YOUR DIFFICULITY: 1:easy  2:Hard  3:IMPOSSIBLE: >"))
    if diff == 1:
        print("YOU HAVE 10 LIVES")
        return 10
    elif diff == 2:
        print("YOU HAVE 5 LIVES")
        return 5
    elif diff == 3:
        print("YOU HAVE 1 Life")
        return 1


def user_guess(attempts):
    NUM_TO_GUESS = random.randint(1, 100)
    guessed = False
    while not guessed:
        guess = int(input("GUESS THE NUMBER: >"))
        if guess > NUM_TO_GUESS:
            print("LOWER!")
            attempts -= 1
            print(f"{attempts} attempts left")
        elif guess < NUM_TO_GUESS:
            print("HIGHER!")
            attempts -= 1
            print(f"{attempts} attempts left")
        elif guess == NUM_TO_GUESS:
            print("YOU WIN")
            print(f"The number was:{NUM_TO_GUESS}")
            if play_again() == True:
                user_guess(attempt_checker())
            guessed = True
        if attempts <= 0:
            print("You Lose")
            print(f"The number was:{NUM_TO_GUESS}")
            if play_again() == True:
                user_guess(attempt_checker())


user_guess(attempt_checker())
