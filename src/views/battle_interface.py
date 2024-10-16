import tkinter as tk
from tkinter import Canvas, PhotoImage

def open_battle_interface():
    battle_window = tk.Toplevel()
    battle_window.title('FirstFight')
    battle_window.geometry('1024x768')

    background_main_window = PhotoImage(file="assets/ForestBackgroundmain.png")

    canvas_main_window = Canvas(battle_window)
    canvas_main_window.pack(fill='both', expand=True)
    canvas_main_window.create_image(0, 0, image=background_main_window, anchor='nw')

    canvas_main_window.image = background_main_window

    # obraz gracza
    player_icon = PhotoImage(file="assets/player_portrait.png")
    player_icon_label = tk.Label(battle_window, image=player_icon, bg='black')
    player_icon_label.place(x=100, y=70)

    player_icon_label.image = player_icon

    # obraz wroga
    enemy_icon = PhotoImage(file="assets/enemy_portrait.png")
    enemy_icon_label = tk.Label(battle_window, image=enemy_icon, bg='black')  # Użyj canvas_main_window jako rodzica
    enemy_icon_label.place(x=604, y=70)

    enemy_icon_label.image = enemy_icon  # Zapisz referencję do obrazu, aby nie został zbędny

