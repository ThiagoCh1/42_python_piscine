def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sorts artifacts by power. Returns empty list on error."""
    try:
        return sorted(
            artifacts,
            key=lambda artifact: artifact['power'],
            reverse=True
        )
    except (KeyError, TypeError) as e:
        print(f"Error sorting artifacts: {e}")
        return []


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filters mages by power. Returns empty list on error."""
    try:
        return list(filter(lambda m: m['power'] >= min_power, mages))
    except (KeyError, TypeError) as e:
        print(f"Error filtering mages: {e}")
        return []


def spell_transformer(spells: list[str]) -> list[str]:
    """Transforms spell names. Returns empty list on error."""
    try:
        return list(map(lambda s: '* ' + str(s) + ' *', spells))
    except TypeError as e:
        print(f"Error transforming spells: {e}")
        return []


def mage_stats(mages: list[dict]) -> dict:
    """Calculates stats. Handles empty lists and bad data gracefully."""
    empty_stats = {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    if not mages:
        return empty_stats

    try:
        max_p = max(mages, key=lambda m: m['power'])['power']
        min_p = min(mages, key=lambda m: m['power'])['power']
        avg_p = round(sum(map(lambda m: m['power'], mages)) / len(mages), 2)
        return {
            'max_power': max_p,
            'min_power': min_p,
            'avg_power': avg_p
        }
    except (KeyError, TypeError, ValueError) as e:
        print(f"Error calculating stats: {e}")
        return empty_stats


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
