# Ten plik odpowiada za logikę biznesową działania sklepu, w tym obsługę zakupu przedmiotów przez gracza.
class ShopController:
    def __init__(self, player_character, view_manager):
        self.player_character = player_character
        self.view_manager = view_manager

    def buy_item(self, item):
        if self.player_character.gold >= item[1]:
            self.player_character.gold -= item[1]
            self.player_character.attack += item[2]
            self.view_manager.update_gold_amount()
            self.view_manager.update_attack()