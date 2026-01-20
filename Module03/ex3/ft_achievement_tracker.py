def achievements() -> None:
    """
    Track and analyze player achievements using set operations.

    Stores unique achievements for multiple players, calculates statistics
    like total unique achievements, and performs set comparisons to find
    common, rare (unique to one player), and differential achievements.
    """
    alice: set[str] = {
        "first_kill", "level_10", "treasure_hunter", "speed_demon"
    }

    bob: set[str] = {
        "first_kill", "level_10", "boss_slayer", "collector"
    }

    charlie: set[str] = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    }

    players: dict[str, set[str]] = {
        "alice": alice,
        "bob": bob,
        "charlie": charlie
    }

    print("=== Achievement Tracker System ===\n")
    for name in players:
        print(f"Player {name} achievements: {players[name]}")

    print("\n=== Achievement Analytics ===")
    uniques: set[str] = alice.union(bob).union(charlie)
    print(f"All unique achievements: {uniques}")
    print(f"Total unique achievements: {len(uniques)}\n")

    common: set[str] = alice.intersection(bob).intersection(charlie)
    print(f"Common to All players: {common}")

    rare: set[str] = alice.difference(bob).difference(charlie)
    rare = rare.union(bob.difference(alice).difference(charlie))
    rare = rare.union(charlie.difference(alice).difference(bob))
    print(f"Rare achievements (1 player): {rare}\n")

    ab: set[str] = alice.intersection(bob)
    print(f"Alice vs Bob common: {ab}")
    aui: set[str] = alice.difference(bob)
    print(f"Alice unique: {aui}")
    bui: set[str] = bob.difference(alice)
    print(f"Bob unique: {bui}")


if __name__ == "__main__":
    achievements()
