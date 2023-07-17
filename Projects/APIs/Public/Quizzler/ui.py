from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzlerInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quizz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR, pady=50, padx=50)

        self.canvas = Canvas(width=600, height=250, bg='white', )
        self.question = self.canvas.create_text(300, 125, text='hold', font=("Arial", 20, "italic"), fill=THEME_COLOR,
                                                width=560)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.false_image = PhotoImage(file='images/false.png')
        self.true_image = PhotoImage(file='images/true.png')
        self.false = Button(image=self.false_image, highlightthickness=0, command=self.check_answer_false)
        self.true = Button(image=self.true_image, highlightthickness=0, command=self.check_answer_true)
        self.false.grid(row=2, column=0)
        self.true.grid(row=2, column=1)

        self.score = Label(text=f"Score : {self.quizz_brain.score}", fg="white", bg=THEME_COLOR, font=("Comic Sans MS", 20, "bold"))
        self.score.grid(column=1, row=0)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        self.window.config(bg=THEME_COLOR)
        self.score.config(bg=THEME_COLOR)
        if self.quizz_brain.still_has_questions():
            q_text = self.quizz_brain.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"You Have Reached the end\nFinal Score:{self.quizz_brain.score}")
            self.true.config(state='disabled')
            self.false.config(state='disabled')

    def check_answer_false(self):
        is_right = self.quizz_brain.check_answer("false")
        self.give_feedback(is_right)
    def check_answer_true(self):
        is_right = self.quizz_brain.check_answer("true")
        self.give_feedback(is_right)

    def give_feedback(self, right):
        if right:
            self.window.config(bg="green")
            self.score.config(bg="green")
        else:
            self.window.config(bg="red")
            self.score.config(bg="red")
        self.score.config(text=f"Score : {self.quizz_brain.score}")
        self.window.after(1000, self.get_question)


