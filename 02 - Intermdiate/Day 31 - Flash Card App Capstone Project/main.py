import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
ITALIC_FONT = ("Ariel", 40, "italic")
BOLD_FONT = ("Ariel", 60, "bold")

df = pd.read_csv("arabic_words.csv")
to_learn = df.to_dict(orient="records")  # list of dictionaries

current_card = {}


####################### - Next Card - #######################

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)  # accessing a random card
    # print(current_card["Arabic"]) accessing a random word from the card that has been chosen
    canvas1.itemconfig(card_title, text="Arabic", fill="black")
    canvas1.itemconfig(card_word, text=current_card["Arabic"], fill="black")
    # Replacing the random word every time the user presses a button
    canvas1.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


####################### - Flip Card - #######################

def flip_card():
    canvas1.itemconfig(card_title, text="English", fill="white")
    canvas1.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas1.itemconfig(card_background, image=back_image)


####################### - Delete Known Card - #######################
def is_known():
    to_learn.remove(current_card)
    next_card()


####################### - UI SETUP - #######################

window = tk.Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

# Front and Back Canvas Images
canvas1 = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
front_image = tk.PhotoImage(file="images/card_front.png")
back_image = tk.PhotoImage(file="images/card_back.png")
card_background = canvas1.create_image(410, 270, image=front_image)
card_title = canvas1.create_text(400, 150, text="", font=ITALIC_FONT)
card_word = canvas1.create_text(400, 263, text="", font=BOLD_FONT)
canvas1.config(highlightthickness=0)
canvas1.grid(row=0, column=0, columnspan=2)

# Buttons-Images
check_image = tk.PhotoImage(file="images/right.png")
wrong_image = tk.PhotoImage(file="images/wrong.png")

# Buttons
known_button = tk.Button(image=check_image, bd=0, highlightthickness=0, command=is_known)
unknown_button = tk.Button(image=wrong_image, bd=0, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)
unknown_button.grid(row=1, column=0)

#  Generates the random word, sets the title and writes the word on the canvas object before screen showing up
next_card()

window.mainloop()
