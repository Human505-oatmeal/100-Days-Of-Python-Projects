from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
cur_card = {}

try:
    df = pandas.read_csv("/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict("records")
else:
    to_learn = df.to_dict('records')


def flip_card():
    canvas.itemconfig(old, image=image_back)
    canvas.itemconfig(card_title, text="English", font=("Arial", 40, "italic"), fill="white")
    canvas.itemconfig(variable_text, text=cur_card["English"], fill="white")


def new_flashcard():
    global cur_card, flip_timer
    root.after_cancel(flip_timer)
    canvas.itemconfig(old, image=image_front)
    cur_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(variable_text, text=cur_card["French"], fill="black")
    flip_timer = root.after(3000, func=flip_card)


def is_known():
    to_learn.remove(cur_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_flashcard()




root = Tk()


root.title("Flashy")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = root.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
image_front = PhotoImage(file="./images/card_front.png")
image_back = PhotoImage(file="./images/card_back.png")
old = canvas.create_image(400, 263, image=image_front)

card_title = canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))
variable_text = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=new_flashcard)
unknown_button.grid(row=1, column=1)

check_image = PhotoImage(file="./images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=0)



mainloop()
