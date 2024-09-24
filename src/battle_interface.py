import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from src.models.character_model import Character
from src.models.character_model import Playercharacter

def otworz_drugie_okno(postac1: Character, postac2: Playercharacter):
    ekran2 = tk.Toplevel()
    ekran2.title("Drugie okno")
    ekran2.geometry("800x800")
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
    label_player_name = tk.Label(ekran2, text=f"Player {postac1.name}", font=("Arial", 14))
    label_player_name.grid(row=1, column=1, padx=10, pady=10)
    label_player_name = tk.Label(ekran2, text=f"Player {postac2.name}", font=("Arial", 14))
    label_player_name.grid(row=1, column=4, padx=10, pady=10)

    # Wywołujemy funkcję, aby obraz wyświetlił się od razu po otwarciu okna
    pokaz_obraz(postac1.picURL)
    pokaz_obraz2(postac2.picURL)

    label_stats = tk.Label(ekran2, text="Player 1 Statistics:", font=("Arial", 14))
    label_stats.grid(row=2, column=1, padx=10, pady=10)
    label_stats = tk.Label(ekran2, text="Player 2 Statistics:", font=("Arial", 14))
    label_stats.grid(row=2, column=4, padx=10, pady=10)

    label_health = tk.Label(ekran2, text=f"Your health: {postac1.hp_player}", font=("Arial", 14))
    label_health.grid(row=3, column=1, padx=10, pady=10)
    label_health = tk.Label(ekran2, text=f"Your health: {postac2.hp_player}", font=("Arial", 14))
    label_health.grid(row=3, column=4, padx=10, pady=10)

    label_attack = tk.Label(ekran2, text=f"Attack power: {postac1.attack_player}", font=("Arial", 14))
    label_attack.grid(row=4, column=1, padx=10, pady=10)
    label_attack = tk.Label(ekran2, text=f"Attack power: {postac2.attack_player}", font=("Arial", 14))
    label_attack.grid(row=4, column=4, padx=10, pady=10)

    label_defense = tk.Label(ekran2, text=f"Defense: {postac1.defense_player}", font=("Arial", 14))
    label_defense.grid(row=5, column=1, padx=10, pady=10)
    label_defense = tk.Label(ekran2, text=f"Defense: {postac2.defense_player}", font=("Arial", 14))
    label_defense.grid(row=5, column=4, padx=10, pady=10)

    button_close = tk.Button(ekran2, text="Zamknij", command=ekran2.destroy)
    button_close.grid(row=6, column=2, padx=10, pady=10)
