from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ''
timer = None



# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global marks
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(counter, text=f"00:00")
    timer_text.config(text="Timer", fg=GREEN)
    marks = ''
    done_label['text'] = marks


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global marks
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        timer_text.config(text="Long Break Time", fg="blue")
        marks += '✓'
        done_label['text'] = marks
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        timer_text.config(text="Small Break Time", fg=GREEN)
        marks += '✓'
        done_label['text'] = marks
    else:
        count_down(WORK_MIN * 60)
        timer_text.config(text="Work Time", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    seconds = count % 60
    minute = math.floor(count / 60)
    if seconds < 10:
        seconds = '0' + f'{seconds}'
    canvas.itemconfig(counter, text=f"{minute}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(bg=YELLOW, padx=100, pady=100)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
counter = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, '30', 'bold'))
canvas.grid(row=1, column=1)

timer_text = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, '20', 'bold'))
timer_text.grid(row=0, column=1)

start_button = Button(text="Start", bg=YELLOW, fg="black", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", fg="black", bg=YELLOW, command=reset)
reset_button.grid(row=2, column=2)

done_label = Label(text="", fg=GREEN, font=(FONT_NAME, '20', 'bold'), bg=YELLOW, highlightthickness=0)
done_label.grid(row=2, column=1)

window.mainloop()
