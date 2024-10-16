# Ten plik odpowiada za inicjalizację i konfigurację głównego widoku sklepu, w tym utworzenie okna i podstawowych elementów GUI.
import tkinter as tk
from src.modules.shop.shop_controller import ShopController
from src.modules.shop.shop_view_manager import ShopViewManager

# Konfiguracja rozmiaru okna
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768

def open_shop(main_window, gold_amount_label, player_character):
    main_window.withdraw()

    shop_window = tk.Toplevel()
    shop_window.title('Shop')
    shop_window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')

    view_manager = ShopViewManager(shop_window, player_character)
    controller = ShopController(player_character, view_manager)

    view_manager.render_shop_background()
    view_manager.render_statistics(gold_amount_label)
    view_manager.render_items(controller.buy_item)
    view_manager.render_exit_button(main_window)