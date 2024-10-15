import tkinter as tk
from tkinter import Canvas, PhotoImage
from src.models.items import Sword
from src.models.character_model import hp, defense, attack, gold

def open_shop(main_window, gold_amount_label):  # Otrzymuje okno główne jako argument
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
        gold_amount_label.config(text=(f": {gold}"))

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
        item_label = tk.Label(shop_window, text=f"+{item.bonus_attack} attack | Price: {item.cost}", bg='grey', font=("Arial", 12))
        item_label.place(x=place_x, y=600)
        item_button = tk.Button(shop_window, image=item_image, command=lambda: buy_item(item))
        item_button.image = item_image
        item_button.place(x=place_x + 26, y=640)

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

    start_place_x = 216
    for i in range(len(swords)):
        show_item_in_shop(swords[i], start_place_x)
        start_place_x += 200

    exit_button = tk.Button(shop_window, text="exit", font=("Ariel", 16), bg="grey", command=lambda: exit_shop(shop_window, main_window))
    exit_button.place(x=50, y=20)

def exit_shop(shop_window, main_window):
    shop_window.destroy()
    main_window.deiconify()



