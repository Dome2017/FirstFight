import tkinter as tk


# Funkcja otwierająca drugie okno
def otworz_drugie_okno(name):
    drugie_okno = tk.Toplevel()  # Tworzymy nowe okno
    drugie_okno.title("Drugie okno")
    drugie_okno.geometry("300x200")

    # Dodajemy label w drugim oknie
    label = tk.Label(drugie_okno, text=f"your name is {name}", font=("Arial", 14))
    label.pack(pady=20)

    # Przykładowy przycisk w drugim oknie
    button = tk.Button(drugie_okno, text="Zamknij", command=drugie_okno.destroy)
    button.pack(pady=10)