import tkinter
import pyperclip
import json
from tkinter import messagebox
from random import randint

path = "logo.png"


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


def save_password():
    fields = [i1_field, i2_field, i3_field]
    data = [field.get() for field in fields]
    new_data = {data[0]: {
        "email": data[1],
        "password": data[2],
        }
    }

    if all(data):
        is_okay = messagebox.askokcancel(title=f"{data[0]}",
                                         message=f"These are the details entered: \nEmail: {data[1]} "
                                                 f"\nPassword: {data[2]}\nIs it ok to save?")
        if is_okay:
            try:
                with open("data.json", "r") as file:
                    data_file = json.load(file)
                    data_file.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            except json.JSONDecodeError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data_file.update(new_data)

                with open("data.json", "w") as file:
                    json.dump(data_file, file, indent=4)
            finally:
                for field in fields:
                    field.delete(0, 'end')
        else:
            pass
    else:
        messagebox.showerror(title="Error", message="Please don't leave any of the fields empty!")


def search_password():
    website = i1_field.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file not found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Data not found.", message="Can't find data.")


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

b3_button = tkinter.Button(text="Search", width=16, command=search_password)
b3_button.grid(row=1, column=2, columnspan=2, pady=5, sticky="WNS")


root.mainloop()
