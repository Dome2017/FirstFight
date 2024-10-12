import tkinter as tk
from tkinter import Canvas, PhotoImage
from src.models.items import Sword

main_window = None
gold = 100
hp = 100
attack = 10
defense = 20

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

    gold_icon = PhotoImage(file='assets/coin_04.png')

    gold_icon_label = tk.Label(main_window, image=gold_icon )
    gold_icon_label.place(x=900, y=10)
    gold_amount = tk.Label(main_window, text=(f": {gold}"), bg='grey', font=("Arial", 16))
    gold_amount.place(x=940, y=12)

    gold_icon.image = gold_icon

    global welcome_label
    welcome_label = tk.Label(main_window, text="Witaj w grze FirstFight!", font=("Arial", 24), bg='green')
    welcome_label.place(x=300, y=100)

    shop_button = tk.Button(main_window, text='Go to the shop', command=open_shop)
    shop_button.place(x=450, y=250)

    close_button = tk.Button(main_window, text="Zamknij okno", command=lambda: close_second_window(main_window))
    close_button.place(x=450, y=300)

def open_shop():
    main_window.withdraw()

    shop_window = tk.Toplevel()
    shop_window.title('Shop')
    shop_window.geometry('1024x768')

    shop_background = PhotoImage(file='assets/storestore.png')

    canvas_shop = Canvas(shop_window)
    canvas_shop.pack(fill='both', expand=True)
    canvas_shop.create_image(0, 0, image=shop_background, anchor='nw')

    canvas_shop.image = shop_background

    swords = [
        Sword("Podstawowy miecz", 10, 10, "assets/testsword_001.png"),
        Sword("Dobry miecz", 20, 20, "assets/testsword_002.png"),
        Sword("Legendarny miecz", 50, 50, "assets/testsword_003.png")
    ]



    def update_gold_amount():
        gold_amount.config(text=(f": {gold}"))

    def update_attack():
        attack_display.config(text=(f"attack power: {attack}"))

    def buy_item(item: Sword):
        global gold, attack
        if gold >= item.cost:
            gold -= item.cost
            attack += item.bonus_attack
            update_gold_amount()
            update_attack()

    def show_item_in_shop(item: Sword, place_x: int):
        item_image = PhotoImage(file=item.picture)
        item_label = tk.Label(shop_window, text=f"+{item.bonus_attack} attack | Price: {item.cost}", bg='grey',font=("Arial", 12))
        item_label.place(x=place_x, y=600)
        item_button = tk.Button(shop_window, image=item_image, command=lambda: buy_item(item))
        item_button.image = item_image
        item_button.place(x=place_x + 26, y=640)

    # Etykiety wyświetlające statystyki
    statistics = tk.Label(shop_window, text=("STATYSTYKI"), font=("Arail", 16), bg="grey")
    statistics.place(x=30, y=370)

    hp_display = tk.Label(shop_window, text=(f"health: {hp}"), font=("Ariel", 16), bg="grey")
    hp_display.place(x=30, y=400)

    attack_display = tk.Label(shop_window, text=(f"attack power: {attack}"), font=("Ariel", 16), bg="grey")
    attack_display.place(x=30, y=430)

    defense_display = tk.Label(shop_window, text=(f"defense: {defense}"), font=("Ariel", 16), bg="grey")
    defense_display.place(x=30, y=460)

    gold_icon = PhotoImage(file='assets/coin_04.png')

    gold_icon_label = tk.Label(shop_window, image=gold_icon)
    gold_icon_label.place(x=900, y=10)
    gold_amount = tk.Label(shop_window, text=(f": {gold}"), bg='grey', font=("Arial", 16))
    gold_amount.place(x=940, y=12)

    gold_icon.image = gold_icon

    # wyświetlenie pozycji w sklepie

    start_place_x = 216
    for i in range(len(swords)):
        show_item_in_shop(swords[i], start_place_x)
        start_place_x += 200

    exit_button = tk.Button(shop_window, text="exit", font=("Ariel", 16), bg="grey", command=lambda: exit_shop(shop_window))
    exit_button.place(x=50, y=20)

def exit_shop(shop_window):
    # Ukryj okno sklepu
    shop_window.destroy()
    # Pokaż ponownie główne okno gry
    main_window.deiconify()


def close_second_window(window):
    # Zamknij nowe okno
    window.destroy()

    # Przywróć główne okno
    interface.deiconify()


# ekran startowy

interface = tk.Tk()
interface.title('Interface')
interface.geometry('500x500')
bg = PhotoImage(file='assets/ForestBackground.png')
canvas_main = Canvas(interface)
canvas_main.pack(fill='both', expand=True)
canvas_main.create_image(0, 0, image=bg, anchor='nw')

welcome_label = tk.Label(text='Welcome to the FIRSTFIGHT',font=('Arial',16),bg='green')
welcome_label.place(x=120,y=100)

name_label = tk.Label(text='Enter your name:', font=('Arial', 12), bg='green')
name_label.place(x=100, y=250)
enter_player_name = tk.Entry(font=('Arial', 12))
enter_player_name.place(x=250, y=250)

start_game_button = tk.Button(text='Start Game', font=('Arial',16),bg='green', command=open_second_window)
start_game_button.place(x=190,y=300)

close_game_button = tk.Button(text='Exit', font=('Arial',16),bg='green', command=exit)
close_game_button.place(x=230,y=350)


interface.mainloop()

