from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power) -> Card:
        if isinstance(name_or_power, str):
            if name_or_power == "dragon":
                creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
            else:
                creature = CreatureCard("Goblin Warrior", 2, "Common", 2, 2)
        elif isinstance(name_or_power, int):
            if name_or_power > 4:
                creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
            else:
                creature = CreatureCard("Goblin Warrior", 2, "Common", 2, 2)
        else:
            name_or_power = "whisper"
            creature = CreatureCard("Whisper", 1, "Common", 1, 1)
        return creature

    def create_spell(self, name_or_power) -> Card:
        if isinstance(name_or_power, str):
            if name_or_power == "fireball":
                spell = SpellCard("Fireball", 6, "Epic",
                                  "Deal 8 damage to target", 8)
            else:
                spell = SpellCard("Lightning Bolt", 3, "Common",
                                  "Deal 3 damage to target", 3)
        elif isinstance(name_or_power, int):
            if name_or_power == "fireball":
                spell = SpellCard("Fireball", 6, "Epic",
                                  "Deal 8 damage to target", 8)
            else:
                spell = SpellCard("Lightning Bolt", 3, "Common",
                                  "Deal 3 damage to target", 3)
        else:
            name_or_power = "night"
            spell = SpellCard("Night Fire", 1, "Common",
                              "Deal 1 damage to target", 1)
        return spell
