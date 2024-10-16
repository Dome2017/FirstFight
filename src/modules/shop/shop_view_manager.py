# Ten plik odpowiada za zarządzanie widokiem sklepu, w tym renderowanie poszczególnych elementów GUI, takich jak tło, statystyki, przedmioty oraz przyciski.
import tkinter as tk
from tkinter import Canvas, PhotoImage


def exit_shop(shop_window, main_window):
    shop_window.destroy()
    main_window.deiconify()


class ShopViewManager:
    def __init__(self, shop_window, player_character):
        self.shop_window = shop_window
        self.player_character = player_character
        self.gold_amount_label = None
        self.attack_display = None

    def render_shop_background(self):
        shop_background = PhotoImage(file='assets/storestore.png')
        canvas_shop = Canvas(self.shop_window)
        canvas_shop.pack(fill='both', expand=True)
        canvas_shop.create_image(0, 0, image=shop_background, anchor='nw')
        canvas_shop.image = shop_background

    def render_statistics(self, gold_amount_label):
        statistics = tk.Label(self.shop_window, text="STATYSTYKI", font=("Arail", 16), bg="grey")
        statistics.place(x=30, y=370)

        hp_display = tk.Label(self.shop_window, text=f"health: {self.player_character.hp}", font=("Ariel", 16), bg="grey")
        hp_display.place(x=30, y=400)

        self.attack_display = tk.Label(self.shop_window, text=f"attack power: {self.player_character.attack}", font=("Ariel", 16), bg="grey")
        self.attack_display.place(x=30, y=430)

        defense_display = tk.Label(self.shop_window, text=f"defense: {self.player_character.defense}", font=("Ariel", 16), bg="grey")
        defense_display.place(x=30, y=460)

        gold_icon = PhotoImage(file='assets/coin_04.png')
        gold_icon_label = tk.Label(self.shop_window, image=gold_icon)
        gold_icon_label.place(x=900, y=10)
        self.gold_amount_label = tk.Label(self.shop_window, text=f": {self.player_character.gold}", bg='grey', font=("Arial", 16))
        self.gold_amount_label.place(x=940, y=12)
        gold_icon_label.image = gold_icon

    def render_items(self, buy_item_callback):
        swords = [
            ("Podstawowy miecz", 10, 10, "assets/testsword_001.png"),
            ("Dobry miecz", 20, 20, "assets/testsword_002.png"),
            ("Legendarny miecz", 50, 50, "assets/testsword_003.png")
        ]
        start_place_x = 216
        for i, (name, cost, bonus_attack, picture) in enumerate(swords):
            item_image = PhotoImage(file=picture)
            item_label = tk.Label(self.shop_window, text=f"+{bonus_attack} attack | Price: {cost}", bg='grey', font=("Arial", 12))
            item_label.place(x=start_place_x + (i * 200), y=600)
            item_button = tk.Button(self.shop_window, image=item_image, command=lambda item=(name, cost, bonus_attack, picture): buy_item_callback(item))
            item_button.image = item_image
            item_button.place(x=start_place_x + 26 + (i * 200), y=640)



    def update_gold_amount(self):
        self.gold_amount_label.config(text=f": {self.player_character.gold}")

    def update_attack(self):
        self.attack_display.config(text=f"attack power: {self.player_character.attack}")

    def render_exit_button(self, main_window):
        exit_button = tk.Button(self.shop_window, text="exit", font=("Ariel", 16), bg="grey", command=lambda: exit_shop(self.shop_window, main_window))
        exit_button.place(x=50, y=20)

