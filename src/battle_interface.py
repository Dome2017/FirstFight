import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from src.models.character_model import Character

def otworz_drugie_okno(postac1: Character):
    ekran2 = tk.Toplevel()
    ekran2.title("Drugie okno")
    ekran2.geometry("800x800")

    def pokaz_obraz(url):
        response = requests.get(url)

        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img = img.resize((300, 350))
            img_tk = ImageTk.PhotoImage(img)
            img_label = tk.Label(ekran2)
            img_label.pack(pady=10)
            img_label.configure(image=img_tk)
            img_label.image = img_tk


############################# Rysowanie Zawartosci ekranu
    label_player_name = tk.Label(ekran2, text=f"Your name is {postac1.name}", font=("Arial", 14))
    label_player_name.pack(pady=20)

    pokaz_obraz('https://as1.ftcdn.net/v2/jpg/05/78/94/44/1000_F_578944489_ZyfZPsK703HOOx8E08NnacYXyMoG7qJY.jpg')  # Wywołujemy funkcję, aby obraz wyświetlił się od razu po otwarciu okna

    label_stats = tk.Label(ekran2, text="Statistics:", font=("Arial", 14))
    label_stats.pack(pady=20)

    label_health = tk.Label(ekran2, text=f"Your health: {postac1.hp_player}", font=("Arial", 14))
    label_health.pack(pady=5)

    label_attack = tk.Label(ekran2, text=f"Attack power: {postac1.attack_player}", font=("Arial", 14))
    label_attack.pack(pady=5)

    label_defense = tk.Label(ekran2, text=f"Defense: {postac1.defense_player}", font=("Arial", 14))
    label_defense.pack(pady=5)

    button_close = tk.Button(ekran2, text="Zamknij", command=ekran2.destroy)
    button_close.pack(pady=10)
