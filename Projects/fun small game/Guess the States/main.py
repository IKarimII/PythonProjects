from turtle import Screen, Turtle
import pandas
from state_drawer import state_drawer

screen = Screen()
screen.setup(width=700, height=490)
screen.addshape("blank_states_img.gif")
image = Turtle("blank_states_img.gif")

guessed = 0
drawer = state_drawer()

guessed_states = []


while guessed < 50:
    user_answer = screen.textinput(title=f"{guessed}/50 Guessed", prompt="Guess A State").title()
    data = pandas.read_csv("50_states.csv")
    states = data['state'].tolist()
    if user_answer in states:
        guessed_states.append(user_answer)
        guessed += 1
        state = data[data.state == user_answer.title()]
        x = int(state.x)
        y = int(state.y)
        drawer.state_draw(user_answer.title(), x, y)
    if user_answer == "Exit":
        missed_states = [state for state in states if state not in guessed_states]
        missed_states_data = pandas.DataFrame(missed_states)
        missed_states_data.to_csv("missed_states")
        print(missed_states)
        break
screen.mainloop()
