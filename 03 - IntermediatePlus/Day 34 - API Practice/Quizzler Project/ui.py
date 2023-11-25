import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = 0
        self.score_label = tk.Label(
            text=f"Score: 0",
            bg=THEME_COLOR,
            fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="quote",
            fill=THEME_COLOR,
            font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = tk.PhotoImage(file="images/true.png")
        false_image = tk.PhotoImage(file="images/false.png")
        self.right_button = tk.Button(
            image=true_image,
            bd=0,
            highlightthickness=0,
            command=lambda: self.check_user_answer(click="true"))
        self.right_button.grid(row=2, column=0)

        self.false_button = tk.Button(
            image=false_image,
            bd=0,
            highlightthickness=0,
            command=lambda: self.check_user_answer(click="false"))
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You reached to the end of the quiz!")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.config(bg="white")

    def check_user_answer(self, click):
        self.give_feedback(self.quiz.check_answer(user_answer=click))

    def give_feedback(self, answer_state):
        if answer_state:
            self.score += 1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
