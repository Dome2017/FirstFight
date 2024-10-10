from tkinter import Canvas, PhotoImage, Tk
import tkinter as tk
from src.models.items import Sword



# lista itemów
swords=[
    Sword("Podstawowy miecz",10,10,"../assets/sword_001.png"),
    Sword("Dobry miecz",20,20,"../assets/sword_002.png"),
    Sword("Legendarny miecz",50,50,"../assets/sword_003.png")
]

gold = 50
hp = 100
attack = 10
defense = 20

root = Tk()
root.geometry("1023x834")
bg = PhotoImage(file="../assets/pixelstorebar.png")

gold_01 = PhotoImage(file="../assets/gold_01.png")
canvas1 = Canvas(root)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")

def update_gold_amount():
    gold_amount.config(text=(f": {gold}"))

def update_attack():
    attack_display.config(text=(f"attack power: {attack}"))

def buy_item(item:Sword):
    global gold, attack
    if gold >= item.cost:
        gold -= item.cost
        attack += item.bonus_attack
        update_gold_amount()
        update_attack()


def show_item_in_shop(item:Sword, place_x:int):
    item_image = PhotoImage(file=item.picture)
    item_label = tk.Label(root, text=f"+{item.bonus_attack} attack | Price: {item.cost}", bg='grey', font=("Arial", 12))
    item_label.place(x=place_x, y=600)
    item_button = tk.Button(root, image=item_image, command=lambda: buy_item(item))
    item_button.image = item_image
    item_button.place(x=place_x - 12, y=640)

# Etykiety wyświetlające statystyki
statistics = tk.Label(root, text=("STATYSTYKI"), font=("Arail", 16), bg="grey")
statistics.place(x=50, y=260)

hp_display = tk.Label(root, text=(f"health: {hp}"), font=("Ariel", 16), bg="grey")
hp_display.place(x=50, y=290)

attack_display = tk.Label(root, text=(f"attack power: {attack}"), font=("Ariel", 16), bg="grey")
attack_display.place(x=50, y=320)

defense_display = tk.Label(root, text=(f"defense: {defense}"), font=("Ariel", 16), bg="grey")
defense_display.place(x=50, y=350)

gold_amount = tk.Label(root, text=(f": {gold}"), bg='grey', font=("Arial", 16))
gold_amount.place(x=870, y=20)
gold_icon = tk.Label(root, image=gold_01)
gold_icon.place(x=840, y=16)

# wyświetlenie pozycji w sklepie

start_place_x = 216
for i in range(len(swords)):
    show_item_in_shop(swords[i],start_place_x)
    start_place_x += 200

def exit():
    root.destroy()

exit_button = tk.Button(root, text="exit", font=("Ariel", 16), bg="grey", command=exit)
exit_button.place(x=50, y=20)

root.mainloop()
