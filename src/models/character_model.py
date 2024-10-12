from dataclasses import dataclass


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