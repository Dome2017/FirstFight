import tkinter as tk
from tkinter import messagebox


def shown_chosen_name():
    character_name = entry.get()
    if character_name.strip() == "":
        messagebox.showerror("Error", "Name must be chosen")
    else:
        input_character_name.config(text=f"You will be {character_name}")



interface = tk.Tk()

interface.title('Interface')
interface.geometry('800x500')

label = tk.Label(interface, text="Weclome to the FirstFight", font=("Arial", 16))
label.grid(row=0, column=2, padx=10, pady=10)

label = tk.Label(interface, text="Chose name of your character!", font=("Arial", 16))
label.grid(row=1, column=1, padx=10, pady=10)

entry = tk.Entry(interface, font =("Arial", 14))
entry.grid(row=1, column=2, padx=10, pady=10)

button = tk.Button(interface, text="ready", font=("Arial", 14), command=shown_chosen_name)
button.grid(row=1, column=3, padx=10, pady=10)

input_character_name = tk.Label(interface, text="", font=("Arial", 14))
input_character_name.grid(row=2, column=1, padx=10, pady=10)

interface.mainloop()