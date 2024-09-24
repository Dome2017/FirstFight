import tkinter as tk
from battle_interface import otworz_drugie_okno
from src.models.character_model import Character

interface = tk.Tk()
interface.title('Interface')
interface.geometry('600x800')
fields = {}

def set_value(napis_przed_input, row, domyslna_wartosc):
    label = tk.Label(interface, text=napis_przed_input, font=("Arial", 16))
    label.grid(row=row, column=1, padx=10, pady=10)

    entry = tk.Entry(interface, font=("Arial", 14))
    entry.grid(row=row, column=2, padx=10, pady=10)
    # Ustawienie domyślnej wartości
    if domyslna_wartosc is not None:
        entry.insert(0, str(domyslna_wartosc))

    return entry

def zapisz_wartosci():
    # 1 postać
    player_character = Character
    player_character.name = fields['name'].get()  # Pobieramy wartość z pola tekstowego
    player_character.picURL = fields['picURL'].get()
    player_character.hp_player = fields['hp'].get()
    player_character.attack_player = fields['attack'].get()
    player_character.defense_player = fields['defense'].get()
    # 2 postać
    player_character2 = Character
    player_character2.name = fields['name2'].get()  # Pobieramy wartość z pola tekstowego
    player_character2.picURL = fields['picURL2'].get()
    player_character2.hp_player = fields['hp2'].get()
    player_character2.attack_player = fields['attack2'].get()
    player_character2.defense_player = fields['defense2'].get()

    otworz_drugie_okno(player_character)



######################## Definicja ekranu

label = tk.Label(interface, text="Welcome to the FirstFight", font=("Arial", 16))
label.grid(row=0, column=2, padx=10, pady=10)

# pola tekstowe zapisu dla postaci nr 1
fields['name'] = set_value('Podaj imie postaci: ', 2,'')
fields['picURL'] = set_value('Podaj URL zdjęcia postaci: ', 3, '')
fields['hp'] = set_value('Podaj życie postaci: ', 4, 100)
fields['attack'] = set_value('Podaj moc ataku postaci: ', 5, 50)
fields['defense'] = set_value("Podaj punkty obrony postaci: ", 6, 20)
# napis sygnalizujący tworzenie 2 postaci
label = tk.Label(interface, text="Druga postać", font=("Arial", 16))
label.grid(row=7, column=2, padx=10, pady=10)
# pola tekstowe zapisu dla postaci nr 2
fields['name2'] = set_value('Podaj imie postaci: ', 8, '')
fields['picURL2'] = set_value('Podaj URL zdjęcia postaci: ', 9, '')
fields['hp2'] = set_value('Podaj życie postaci: ', 10, '')
fields['attack2'] = set_value('Podaj moc ataku postaci: ', 11, '')
fields['defense2'] = set_value("Podaj punkty obrony postaci: ", 12, '')
# przycisk otwarcia drugiego okna
button = tk.Button(interface, text="zaprezentuj postacie", command=zapisz_wartosci)
button.grid(row=14, column=2, pady=20)




interface.mainloop()
