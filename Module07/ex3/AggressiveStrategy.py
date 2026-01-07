from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        card_played: list = []
        mana_used: int = 0
        damage_dealt = 0
        for card in hand[:]:
            if card.cost <= 3:
                card_played.append(card)
                if card.type != "Spell":
                    battlefield.append(card)
                    damage_dealt += card.attack
                else:
                    damage_dealt += card.damage
                mana_used += card.cost
                hand.remove(card)
