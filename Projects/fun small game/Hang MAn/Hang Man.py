import random
import Words
import Logo


word_to_guess = random.choice(Words.words)
Lives = 6
Guessed = []
for i in word_to_guess:
    Guessed.append("_")
guessed_string = ""
letters_guessed = ""
print(Logo.logo)
while Lives :
    indicator = False
    print(Guessed)
    guessed_string = ""
    for letter in Guessed:
        guessed_string += letter
    print("The Words is:",guessed_string)
    print("Letters guessed are: ",letters_guessed)
    if word_to_guess.lower() == guessed_string.lower():
        print("YOU WIN!")
        print("The Word Was: ",word_to_guess.upper())
        break
    print(Logo.hangman[Lives])
    user_guess = input("Type the letter to guess")
    for i in range(0,len(word_to_guess)):
        if user_guess.lower() == word_to_guess[i]:
            Guessed[i] = word_to_guess[i]
            indicator = True

    if indicator == False:
        Lives-=1
        letters_guessed += user_guess.upper()
        print(f"The letter {user_guess} is not in the word")

    if Lives<=0:
        print("YOU LOSE!")
        print("The Word Was: ", word_to_guess.upper())
