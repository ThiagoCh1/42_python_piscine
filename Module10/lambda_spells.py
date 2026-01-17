def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
    Sorts a list of artifacts by their power level in descending order.
    """
    return sorted(artifacts,
                  key=lambda artifact: artifact['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spells: '* ' + spells + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    max_mage = max(mages, key=lambda m: m['power'])
    min_mage = min(mages, key=lambda m: m['power'])
    total_power = sum(map(lambda m: m['power'], mages))
    avg_val = round(total_power / len(mages), 2)
    return {
        'max_power': max_mage,
        'min_power': min_mage,
        'avg_power': avg_val
    }


if __name__ == "__main__":
    print("Testing artifact sorter...")
    test_artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'}
    ]
    sorted_arts = artifact_sorter(test_artifacts)
    print(
        f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) "
        f"comes before "
        f"{sorted_arts[1]['name']} ({sorted_arts[1]['power']} power)"
    )

    print("\nTesting spell transformer...")
    test_spells = ['fireball', 'heal', 'shield']
    for s in spell_transformer(test_spells):
        print(s)

    print("\nTesting power filter & stats...")
    test_mages = [
        {'name': 'Merlin', 'power': 100, 'element': 'light'},
        {'name': 'Gandalf', 'power': 150, 'element': 'light'},
        {'name': 'Apprentice', 'power': 10, 'element': 'water'}
    ]
    print(
        f"Filtered mages (min 50): "
        f"{[m['name'] for m in power_filter(test_mages, 50)]}"
    )
    print(f"Stats: {mage_stats(test_mages)}")
