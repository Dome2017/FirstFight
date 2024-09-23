import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO

hp_player = 100
attack_player = 20
defense_player = 10


def otworz_drugie_okno(name):
    drugie_okno = tk.Toplevel()
    drugie_okno.title("Drugie okno")
    drugie_okno.geometry("800x800")

    label_player_name = tk.Label(drugie_okno, text=f"Your name is {name}", font=("Arial", 14))
    label_player_name.pack(pady=20)

    label_stats = tk.Label(drugie_okno, text="Statistics:", font=("Arial", 14))
    label_stats.pack(pady=20)


    img_label = tk.Label(drugie_okno)
    img_label.pack(pady=10)


    def pokaz_obraz():
        url = 'https://as1.ftcdn.net/v2/jpg/05/78/94/44/1000_F_578944489_ZyfZPsK703HOOx8E08NnacYXyMoG7qJY.jpg'
        response = requests.get(url)

        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img = img.resize((300, 350))
            img_tk = ImageTk.PhotoImage(img)
            img_label.configure(image=img_tk)
            img_label.image = img_tk

    pokaz_obraz()  # Wywołujemy funkcję, aby obraz wyświetlił się od razu po otwarciu okna

    label_health = tk.Label(drugie_okno, text=f"Your health: {hp_player}", font=("Arial", 14))
    label_health.pack(pady=5)

    label_attack = tk.Label(drugie_okno, text=f"Attack power: {attack_player}", font=("Arial", 14))
    label_attack.pack(pady=5)

    label_defense = tk.Label(drugie_okno, text=f"Defense: {defense_player}", font=("Arial", 14))
    label_defense.pack(pady=5)

    button_close = tk.Button(drugie_okno, text="Zamknij", command=drugie_okno.destroy)
    button_close.pack(pady=10)
