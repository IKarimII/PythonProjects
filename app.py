from flask import Flask
import random as rn

number_to_guess = rn.randint(1,9)
print(number_to_guess)
app = Flask(__name__)


@app.route("/")
def welcome():
    return '''Welcome to Number Guesser
        Guess a Number Between 1-9 '''


@app.route("/<number>")
def Guess(number):
    if int(number) == number_to_guess:
        return "YOU GUESSED IT"
    else:
        return "You Didn't guess it "


if __name__ == '__main__':
    app.run()