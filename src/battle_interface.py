import tkinter as tk
from tkinter import Scrollbar, Text
from tkinter.constants import RIGHT

import requests
from PIL import Image, ImageTk
from io import BytesIO
from src.models.character_model import Character
from src.models.character_model import Playercharacter



def otworz_drugie_okno(postac1: Character, postac2: Playercharacter):
    ekran2 = tk.Toplevel()
    ekran2.title("Drugie okno")
    ekran2.geometry("800x1000")


    def aktualizuj_hp_label():
        label_health1.config(text=f"Twoje życie: {postac1.hp_player}")
        label_health2.config(text=f"Twoje życie: {postac2.hp_player}")

    def oblicz_obrażenia(atakujacy, obronca):
        # Konwersja wartości na liczby całkowite przed obliczeniami
        atak_player = int(atakujacy.attack_player)
        obrona_player = int(obronca.defense_player)
        hp_obroncy = int(obronca.hp_player)  # Konwersja HP obrońcy na int

        # Obliczanie obrażeń, ale nie mniej niż 0
        obrazenia = max(atak_player - obrona_player, 0)

        # Aktualizacja HP obrońcy, nie mniej niż 0
        obronca.hp_player = max(hp_obroncy - obrazenia, 0)

        return obrazenia


    # funkcja do obrazu nr 1
    def pokaz_obraz(url):
        response = requests.get(url)

        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img = img.resize((300, 350))
            img_tk = ImageTk.PhotoImage(img)
            img_label = tk.Label(ekran2)
            img_label.grid(row=0, column=1, padx=10, pady=10)
            img_label.configure(image=img_tk)
            img_label.image = img_tk
    # funkcja do obrazu nr 2
    def pokaz_obraz2(url):
        response = requests.get(url)

        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img = img.resize((300, 350))
            img_tk = ImageTk.PhotoImage(img)
            img_label = tk.Label(ekran2)
            img_label.grid(row=0, column=4, padx=10, pady=10)
            img_label.configure(image=img_tk)
            img_label.image = img_tk


    ############################# Rysowanie Zawartosci ekranu
    label_player_name1 = tk.Label(ekran2, text=f"Player {postac1.name}", font=("Arial", 14))
    label_player_name1.grid(row=1, column=1, padx=10, pady=10)
    label_player_name2 = tk.Label(ekran2, text=f"Player {postac2.name}", font=("Arial", 14))
    label_player_name2.grid(row=1, column=4, padx=10, pady=10)

    # Wywołujemy funkcję, aby obraz wyświetlił się od razu po otwarciu okna
    pokaz_obraz(postac1.picURL)
    pokaz_obraz2(postac2.picURL)

    label_stats1 = tk.Label(ekran2, text="Player 1 Statistics:", font=("Arial", 14))
    label_stats1.grid(row=2, column=1, padx=10, pady=10)
    label_stats2 = tk.Label(ekran2, text="Player 2 Statistics:", font=("Arial", 14))
    label_stats2.grid(row=2, column=4, padx=10, pady=10)

    label_health1 = tk.Label(ekran2, text=f"Your health: {postac1.hp_player}", font=("Arial", 14))
    label_health1.grid(row=3, column=1, padx=10, pady=10)
    label_health2 = tk.Label(ekran2, text=f"Your health: {postac2.hp_player}", font=("Arial", 14))
    label_health2.grid(row=3, column=4, padx=10, pady=10)

    label_attack1 = tk.Label(ekran2, text=f"Attack power: {postac1.attack_player}", font=("Arial", 14))
    label_attack1.grid(row=4, column=1, padx=10, pady=10)
    label_attack2 = tk.Label(ekran2, text=f"Attack power: {postac2.attack_player}", font=("Arial", 14))
    label_attack2.grid(row=4, column=4, padx=10, pady=10)

    label_defense1 = tk.Label(ekran2, text=f"Defense: {postac1.defense_player}", font=("Arial", 14))
    label_defense1.grid(row=5, column=1, padx=10, pady=10)
    label_defense2 = tk.Label(ekran2, text=f"Defense: {postac2.defense_player}", font=("Arial", 14))
    label_defense2.grid(row=5, column=4, padx=10, pady=10)

    button_close = tk.Button(ekran2, text="Zamknij", command=ekran2.destroy)
    button_close.grid(row=10, column=2, padx=10, pady=10)

    ############################################### przestrzeń walki
    # Log akcji
    text_frame = tk.Frame(ekran2)
    text_frame.grid(row=9, column=1, columnspan=4, padx=10, pady=10, sticky="nsew")

    scrollbar = Scrollbar(text_frame)
    scrollbar.pack(side=RIGHT, fill=tk.Y)

    # Widget Text do logowania akcji
    text_log = Text(text_frame, height=10, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    text_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=text_log.yview) # Konfiguracja scrollbara do współpracy z Text

    # Funkcja do wyświetlania akcji walki
    def dodaj_akcje_log(tekst):
        text_log.insert(tk.END,"- " + tekst + "\n")
        text_log.see(tk.END)  # Automatyczne przewinięcie do ostatniej akcji

    # Funkcje akcji
    def atak():
        obrazenia = oblicz_obrażenia(postac1, postac2)
        dodaj_akcje_log(f"{postac1.name} atakuje {postac2.name} za {obrazenia} punktów obrażeń ")
        aktualizuj_hp_label()

        if postac2.hp_player <= 0:
            dodaj_akcje_log(f"{postac2.name} został pokonany")

    def obrona():
        dodaj_akcje_log(f"{postac1.name} broni się!")

    def atak_specjalny():
        obrazenia = oblicz_obrażenia(postac1, postac2) * 1.5 # atak specjalny zadaje 50% więcej
        dodaj_akcje_log(f"{postac1.name} używa ataku specjalnego przeciwko {postac2.name} za {obrazenia} punktów obrażeń")
        aktualizuj_hp_label()

        if postac2.hp_player <= 0:
            dodaj_akcje_log(f"{postac2.name} został pokonany")

    # Przyciski akcji
    button_attack = tk.Button(ekran2, text="Atak", command=atak)
    button_attack.grid(row=6, column=2, padx=10, pady=10)

    button_attack = tk.Button(ekran2, text="Obrona", command=obrona)
    button_attack.grid(row=7, column=2, padx=10, pady=10)

    button_attack = tk.Button(ekran2, text="Atak specjalny", command=atak_specjalny)
    button_attack.grid(row=8, column=2, padx=10, pady=10)

