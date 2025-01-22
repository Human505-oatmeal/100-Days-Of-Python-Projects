from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.false_image = PhotoImage(file="./images/false.png")
        self.true_image = PhotoImage(file="./images/true.png")

        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, columnspan=2)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="White", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, pady=15)

        self.button_false = Button(self.window, image=self.false_image, highlightthickness=0, command=self.true_pressed)
        self.button_false.grid(row=2, column=0, pady=30)

        self.button_true = Button(self.window, image=self.true_image, highlightthickness=0, command=self.false_pressed)
        self.button_true.grid(row=2, column=1, pady=30)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="red")
        else:
            self.canvas.config(bg="green")
        self.window.after(1000, self.get_next_question)
        self.score_label.config(text=f"Score: {self.quiz.score}")

