import tkinter as tk
from battle_interface import otworz_drugie_okno
from src.models.character_model import Character

interface = tk.Tk()
interface.title('Interface')
interface.geometry('800x500')
fields = {}

def set_value(napis_przed_input, row):
    label = tk.Label(interface, text=napis_przed_input, font=("Arial", 16))
    label.grid(row=row, column=1, padx=10, pady=10)

    entry = tk.Entry(interface, font=("Arial", 14))
    entry.grid(row=row, column=2, padx=10, pady=10)

    return entry

def zapisz_wartosci():
    player_character = Character
    player_character.name = fields['name'].get()  # Pobieramy wartość z pola tekstowego
    player_character.picURL = fields['picURL'].get()
    player_character.hp_player = fields['hp'].get()
    player_character.attack_player = fields['attack'].get()
    player_character.defense_player = fields['defense'].get()

    otworz_drugie_okno(player_character)



######################## Definicja ekranu

label = tk.Label(interface, text="Welcome to the FirstFight", font=("Arial", 16))
label.grid(row=0, column=2, padx=10, pady=10)


fields['name'] = set_value('Podaj imie postaci: ', 2)
fields['picURL'] = set_value('Podaj URL zdjęcia postaci: ', 3)
fields['hp'] = set_value('Podaj życie postaci: ', 4)
fields['attack'] = set_value('Podaj moc ataku postaci: ', 5)
fields['defense'] = set_value("Podaj punkty obrony postaci: ", 6)

button = tk.Button(interface, text="zaprezentuj postać", command=zapisz_wartosci)
button.grid(row=7, column=2, pady=20)




interface.mainloop()
