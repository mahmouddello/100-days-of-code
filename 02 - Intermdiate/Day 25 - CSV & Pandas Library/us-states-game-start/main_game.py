import turtle
import pandas as pd

ALIGNMENT = "center"
FONT = ("Fire Code", 6, "normal")

df = pd.read_csv('50_states.csv')
writer = turtle.Turtle()
# Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_list = df["state"].to_list()
guessed_states = []


def write_on_map(user_answer):
    writer.penup()
    writer.hideturtle()
    answered_state = df[df["state"] == user_answer]
    state_x = int(answered_state["x"])
    state_y = int(answered_state["y"])
    writer.goto(x=state_x, y=state_y)
    writer.write(f"{user_answer}", align=ALIGNMENT, font=FONT)


# User Answers here
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/{len(states_list)} States Correct",
                              prompt="What's another state's name?").title()
    print(answer)
    if answer == "Exit":
        missed_states = []
        for state in states_list:
            if state not in guessed_states:
                missed_states.append(state)
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer in states_list and answer not in guessed_states:
        guessed_states.append(answer)
        write_on_map(answer)
