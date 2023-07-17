import sys
from tkinter import *
from tkinter import messagebox
import pandas
from random import *
import json

# |-----------------------------------------PANDAS---------------------------------------------------|
with open(file="spanish.csv", mode="r") as file_data:
    data = pandas.read_csv(file_data)
    spanish_words = data['Spanish'].tolist()
    english_words = data['English'].tolist()

    spanish_word = choice(spanish_words)
    english_word = english_words[spanish_words.index(spanish_word)]
    spanish_words.remove(spanish_word)


# |-----------------------------------------Functions---------------------------------------------------|
def rand_spanish_words():
    global spanish_word
    global english_word
    if spanish_words == []:
        messagebox.showwarning(title="Flash Card Game", message="All Words Have Been Used")
        sys.exit()
    spanish_word = choice(spanish_words)
    english_word = english_words[spanish_words.index(spanish_word)]
    spanish_words.remove(spanish_word)

    canvas.itemconfig(language, text='Spanish', fill="black")
    canvas.itemconfig(worded, text=spanish_word, fill='black')
    canvas.itemconfig(image, image=front_image)


def english_wordss():
    canvas.itemconfig(language, text='English', fill="white")
    canvas.itemconfig(worded, text=english_word, fil='white')
    canvas.itemconfig(image, image=back_image)


# |---------------------------------------UI---------------------------------------------------------|
window = Tk()
window.config(padx=50, pady=50, bg="#B1DDC6")
window.title("Flashcard Game")

canvas = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=front_image)
language = canvas.create_text(400, 100, text="Spanish", font=("Comic Sans MS", 40, "italic"))
worded = canvas.create_text(400, 300, text=f"{spanish_word}", font=("Comic Sans MS", 30, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=english_wordss)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=rand_spanish_words)
right_button.grid(column=1, row=1)

window.mainloop()
