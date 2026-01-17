def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """Combines two spells into one function
    that returns a tuple of results."""
    return lambda *args, **kwargs: (
        spell1(*args, **kwargs),
        spell2(*args, **kwargs)
    )


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """Amplifies the result of a spell by a multiplier."""
    return lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    """Casts a spell only if the condition function returns True."""
    return lambda *args, **kwargs: (
        spell(*args, **kwargs) if condition(*args, **kwargs)
        else "Spell fizzled"
    )


def spell_sequence(spells: list[callable]) -> callable:
    """Executes a list of spells in order and returns their results."""
    return lambda *args, **kwargs: [spell(*args, **kwargs) for spell in spells]


if __name__ == "__main__":
    print("Testing spell combiner...")
    def fireball(target): return f"Fireball hits {target}"
    def heal(target): return f"Heals {target}"

    mixed = spell_combiner(fireball, heal)
    print(f"Combined spell result: {mixed('Dragon')}")

    print("\nTesting power amplifier...")
    def zap(power): return power
    mega_zap = power_amplifier(zap, 3)
    print(f"Original: 10, Amplified: {mega_zap(10)}")

    print("\nTesting conditional caster...")
    def is_enemy(target): return target == "Goblin"
    smart_fireball = conditional_caster(is_enemy, fireball)
    print(f"Target Goblin: {smart_fireball('Goblin')}")
    print(f"Target Ally: {smart_fireball('Ally')}")

    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, heal])
    print(f"Sequence: {combo('Hero')}")
