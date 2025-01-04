import tkinter
from tkinter import messagebox
from random import randint
import pyperclip

path = "logo.png"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator(length=12):
    characters = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "1234567890"
        "!@#$%^&*()_+-=[]{}|;:,.<>?/"
        "`~"
    )
    password = [(characters[randint(0, len(characters)-1)]) for _ in range(length)]
    new_pass = "".join(password)
    pyperclip.copy(new_pass)
    pass_var.set(new_pass)



# ---------------------------- SAVE PASSWORD ------------------------------- #


# save passwords in file called "data.txt"

def save_password():
    fields = [i1_field, i2_field, i3_field]
    data = [field.get() for field in fields]

    if all(data):
        is_okay = messagebox.askokcancel(title=f"{data[0]}",
                                         message=f"These are the details entered: \nEmail: {data[1]} "
                                                 f"\nPassword: {data[2]}\nIs it ok to save?")
        if is_okay:
            with open("data.txt", "a+") as file:
                file.write(f"{data[0]} | {data[1]} | {data[2]}\n")
            for field in fields:
                field.delete(0, 'end')
        else:
            pass
    else:
        messagebox.showerror(title="Error", message="Please don't leave any of the fields empty!")


# ---------------------------- UI SETUP ------------------------------- #


root = tkinter.Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)
pass_var = tkinter.StringVar()

# Logo
canvas = tkinter.Canvas(root, width=200, height=200)
try:
    img = tkinter.PhotoImage(file=path)
    canvas.create_image(100, 100, image=img)
except tkinter.TclError:
    canvas.create_text(100, 100, text="Logo Missing", fill="red", font=("Arial", 10))
canvas.grid(row=0, column=1)

# Labels
l1 = tkinter.Label(text="Website:")
l1.grid(row=1, column=0, sticky="E", padx=5, pady=5)

l2 = tkinter.Label(text="Email/Username:")
l2.grid(row=2, column=0, sticky="E", padx=5, pady=5)

l3 = tkinter.Label(text="Password:")
l3.grid(row=3, column=0, sticky="E", padx=5, pady=5)

# Entry Fields
i1_field = tkinter.Entry(width=35)
i1_field.grid(row=1, column=1, columnspan=2, pady=5, sticky="WNS")
i1_field.focus()

i2_field = tkinter.Entry(width=35)
i2_field.grid(row=2, column=1, columnspan=2, pady=5, sticky="WNS")
i2_field.insert(0, "dummy@mail.com")

i3_field = tkinter.Entry(width=35, textvariable=pass_var)
i3_field.grid(row=3, column=1, pady=5, sticky="WNS")

# Buttons
b1_button = tkinter.Button(text="Generate Password", width=16, command=password_generator)
b1_button.grid(row=3, column=2, pady=5, sticky="WNS")

b2_button = tkinter.Button(text="Add", width=50, command=save_password)
b2_button.grid(row=4, column=1, columnspan=2, pady=10, sticky="N")

root.mainloop()
