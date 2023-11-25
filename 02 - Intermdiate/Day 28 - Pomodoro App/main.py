import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_minute = math.floor(count / 60)  # Return the floor of x as an Integral.
    count_second = count % 60  # gets the seconds
    if count_second < 10:
        count_second == f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")  # updates the text in every count
    if count > 0:
        canvas.after(1000, count_down, count - 1)  # Recursion: after 1 sec call the function back


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer label

timer_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

# canvas widget (image)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.grid(column=1, row=1)

# text on canvas
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")

# start-button
start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset-Button

reset_button = tk.Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

# Checkmark
checkmark = tk.Label(text="✅", fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()
