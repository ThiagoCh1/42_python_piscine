from ex0.Card import Card, CardType
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack_points: int,
                 health_points: int, defense_points: int,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.type = CardType.ELITE
        self.attack_points = attack_points
        self.health_points = health_points
        if attack_points < 0 or health_points < 0:
            raise ValueError
        self.effect_type = effect_type

    def attack(self, target) -> dict:
        try:
            name: str = target.name
        except AttributeError:
            raise ValueError
        still_alive: bool
        if self.attack >= target.health:
            still_alive = False
            target.health = 0
        else:
            target.health -= self.attack
            still_alive = True
        result = {"attacker": self.name, "target": name, "damage_dealt":
                  self.attack, "still_alive": still_alive}
        return result
