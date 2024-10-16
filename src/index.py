import tkinter as tk
from tkinter import Canvas, PhotoImage
from src.models.character_model import Character
from src.views.Shop import open_shop  # Usuń `main_window` z importu
from src.views.battle_interface import open_battle_interface

main_window = None
gold_amount_label = None

def open_second_window():
    global main_window
    # Ukryj główne okno
    interface.withdraw()

    main_window = tk.Toplevel()
    main_window.title('FirstFight')
    main_window.geometry('1024x768')

    background_main_window = PhotoImage(file="assets/ForestBackgroundmain.png")

    canvas_main_window = Canvas(main_window)
    canvas_main_window.pack(fill='both', expand=True)
    canvas_main_window.create_image(0, 0, image=background_main_window, anchor='nw')

    canvas_main_window.image = background_main_window

    player_name = enter_player_name.get()

    global player_character
    player_character = Character(player_name,100, 10, 5, 50)

    gold_icon = PhotoImage(file='assets/coin_04.png')

    gold_icon_label = tk.Label(main_window, image=gold_icon)
    gold_icon_label.place(x=900, y=10)
    gold_amount_label = tk.Label(main_window, text=(f": {player_character.gold}"), bg='grey', font=("Arial", 16))
    gold_amount_label.place(x=940, y=12)
    gold_icon.image = gold_icon

    welcome_label = tk.Label(main_window, text="Witaj w grze FirstFight!", font=("Arial", 24), bg='green')
    welcome_label.place(x=300, y=100)

    start_first_duel = tk.Button(main_window, text='Begin fight', command=lambda: open_battle_interface())
    start_first_duel.place(x=450, y=200)

    shop_button = tk.Button(main_window, text='Go to the shop', command=lambda: open_shop(main_window, gold_amount_label, player_character))  # Przekazanie okna jako argument
    shop_button.place(x=450, y=250)

    close_button = tk.Button(main_window, text="Zamknij okno", command=lambda: close_second_window(main_window))
    close_button.place(x=450, y=300)

def close_second_window(window):
    window.destroy()
    interface.deiconify()

interface = tk.Tk()
interface.title('Interface')
interface.geometry('500x500')
bg = PhotoImage(file='assets/ForestBackground.png')
canvas_main = Canvas(interface)
canvas_main.pack(fill='both', expand=True)
canvas_main.create_image(0, 0, image=bg, anchor='nw')

welcome_label = tk.Label(text='Welcome to the FIRSTFIGHT', font=('Arial', 16), bg='green')
welcome_label.place(x=120, y=100)

name_label = tk.Label(text='Enter your name:', font=('Arial', 12), bg='green')
name_label.place(x=100, y=250)
enter_player_name = tk.Entry(font=('Arial', 12))
enter_player_name.place(x=250, y=250)

start_game_button = tk.Button(text='Start Game', font=('Arial', 16), bg='green', command=open_second_window)
start_game_button.place(x=190, y=300)

close_game_button = tk.Button(text='Exit', font=('Arial', 16), bg='green', command=exit)
close_game_button.place(x=230, y=350)

interface.mainloop()


