def achievements():
    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}

    bob = {"first_kill", "level_10", "boss_slayer", "collector"}

    charlie = {
     "level_10",
     "treasure_hunter",
     "boss_slayer",
     "speed_demon",
     "perfectionist"
    }

    players = {
        "alice": alice,
        "bob": bob,
        "charlie": charlie
    }

    print("=== Achievement Tracker System ===\n")
    for name in players:
        print(f"Player {name} achievements: {players[name]}")

    print("\n=== Achievement Analytics ===")
    uniques = alice.union(bob).union(charlie)
    print(f"All unique achievements: {uniques}")
    print(f"Total unique achievements: {len(uniques)}\n")

    common = alice.intersection(bob).intersection(charlie)
    print(f"Common to All players: {common}")
    rare = alice.difference(bob).difference(charlie)
    rare = rare.union(bob.difference(alice).difference(charlie))
    rare = rare.union(charlie.difference(alice).difference(bob))
    print(f"Rare achievements (1 player): {rare}\n")

    ab = alice.intersection(bob)
    print(f"Alice vs Bob common: {ab}")
    aui = alice.difference(bob)
    print(f"Alice unique: {aui}")
    bui = bob.difference(alice)
    print(f"Bob unique: {bui}")


if __name__ == "__main__":
    achievements()
