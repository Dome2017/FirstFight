from tkinter import Canvas, PhotoImage, Tk
import tkinter as tk
gold = 50
hp = 100
attack = 10
defense = 20

root = Tk()
root.geometry("1023x834")
bg = PhotoImage(file="pixelstorebar.png")
sword_1 = PhotoImage(file="sword_001.png")
sword_2 = PhotoImage(file="sword_002.png")
sword_3 = PhotoImage(file="sword_003.png")
gold_01 = PhotoImage(file="gold_01.png")
canvas1 = Canvas(root)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg,anchor="nw")


def update_gold_amount():
    gold_amount.config(text=(f": {gold}"))
def update_attack():
    attack_display.config(text=(f"attack power: {attack}"))

def kup1():
    global gold,attack
    if gold >= 10:
        gold -= 10
        attack += 10
        update_gold_amount()
        update_attack()

def kup2():
    global gold,attack
    if gold >= 20:
        gold -= 20
        attack += 20
        update_gold_amount()
        update_attack()

def kup3():
    global gold,attack
    if gold >= 50:
        gold -= 50
        attack += 50
        update_gold_amount()
        update_attack()

statistics = tk.Label(root,text=("STATYSTYKI"), font=("Arail",16),bg="grey")
statistics.place(x=50,y=260)

hp_display = tk.Label(root, text=(f"health: {hp}"),font=("Ariel",16), bg="grey")
hp_display.place(x=50,y=290)

attack_display = tk.Label(root, text=(f"attack power: {attack}"),font=("Ariel",16), bg="grey")
attack_display.place(x=50,y=320)

defense_display = tk.Label(root, text=(f"defense: {defense}"),font=("Ariel",16), bg="grey")
defense_display.place(x=50,y=350)

gold_amount = tk.Label(root, text=(f": {gold}"), bg='grey', font=("Arial", 16))
gold_amount.place(x=870, y=20)
gold_icon = tk.Label(root,image=gold_01)
gold_icon.place(x=840,y=16)
info_przycisk_miecz_1 = tk.Label(root, text="+10 attack | Price: 10", bg='grey', font=("Arial", 12))
info_przycisk_miecz_1.place(x=216,y=600)
przycisk_miecz_2 = tk.Button(root, image=sword_1, command=kup1)
przycisk_miecz_2.place(x=204,y=640)
info_przycisk_miecz_1 = tk.Label(root, text="+20 attack | Price: 20", bg='grey', font=("Arial", 12))
info_przycisk_miecz_1.place(x=414,y=600)
przycisk_miecz_2 = tk.Button(root, image=sword_2, command=kup2)
przycisk_miecz_2.place(x=408,y=640)
info_przycisk_miecz_3 = tk.Label(root, text="+50 attack | Price: 50", bg='grey', font=("Arial", 12))
info_przycisk_miecz_3.place(x=618,y=600)
przycisk_miecz_3 = tk.Button(root, image=sword_3, command=kup3)
przycisk_miecz_3.place(x=612,y=640)
def exit():
    root.destroy()
exit_button = tk.Button(root, text="exit", font=("Ariel",16), bg="blue", command=exit)
exit_button.place(x=50, y=20)

root.mainloop()