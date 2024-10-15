from dataclasses import dataclass
gold = 100
hp = 100
attack = 10
defense = 20

@dataclass
class Character:
    name: str
    picURL: str
    hp_player: int
    attack_player: int
    defense_player: int

@dataclass
class Playercharacter:
    name: str
    picURL: str
    hp_player: int
    attack_player: int
    defense_player: int