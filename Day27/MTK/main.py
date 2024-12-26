import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.resizable(width=False, height=False)
window.geometry("300x150")
window.config(padx=45,pady=25)


def miles_to_km():
    miles = float(Entry.get())
    result = miles * 1.6
    Output.config(text=f"{result:.2f}")


Label_Miles = tkinter.Label(text="Miles", font=("Arial", 12))
Label_Miles.grid(column=2, row=0)

Entry = tkinter.Entry(width=10)
Entry.grid(column=1, row=0)

Label = tkinter.Label(text="is equal to", font=("Arial", 12, "italic"))
Label.grid(column=0, row=1)

Output = tkinter.Label(text="0", font=("Arial", 12))
Output.grid(column=1, row=1)

Label_Km = tkinter.Label(text="Km", font=("Arial", 12))
Label_Km.grid(column=2, row=1)

Button = tkinter.Button(text="Calculate", command=miles_to_km)
Button.grid(column=1, row=2)

window.mainloop()
