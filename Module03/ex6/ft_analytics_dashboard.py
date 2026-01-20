def main() -> None:
    """
    Run the analytics dashboard using various Python comprehensions.

    Demonstrates list, dictionary, and set comprehensions to filter,
    transform, and analyze game data without traditional loops.
    """
    print("=== Game Analytics Dashboard ===")

    scores: dict[str, int] = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050
    }

    sessions: list[dict] = [
        {"player": "alice", "mode": "ranked", "completed": True},
        {"player": "bob", "mode": "casual", "completed": True},
        {"player": "charlie", "mode": "competitive", "completed": False},
        {"player": "charlie", "mode": "ranked", "completed": True},
        {"player": "diana", "mode": "casual", "completed": True}
    ]

    achievements: dict[str, set[str]] = {
        "alice": {
            "first_kill", "level_10", "treasure_hunter",
            "speed_demon", "boss_slayer"
        },
        "bob": {
            "first_kill", "level_10", "collector"
        },
        "charlie": {
            "level_10", "boss_slayer", "perfectionist",
            "speed_demon", "treasure_hunter",
            "explorer", "strategist"
        },
        "diana": {
            "first_kill", "level_10",
            "boss_slayer", "treasure_hunter"
        }
    }

    regions: dict[str, str] = {
        "alice": "north",
        "bob": "east",
        "charlie": "central",
        "diana": "east"
    }

    print("\n=== List Comprehension Examples ===")

    high_scorers: list[str] = [p for p in scores if scores[p] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores: list[int] = [scores[p] * 2 for p in scores]
    print(f"Scores doubled: {doubled_scores}")

    active_players: list[str] = sorted({
        s["player"] for s in sessions if s["completed"]
    })
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores: dict[str, int] = {p: scores[p] for p in scores}
    print(f"Player scores: {player_scores}")

    score_categories: dict[str, int] = {
        "high": len([p for p in scores if scores[p] > 2000]),
        "medium": len([
            p for p in scores
            if 1500 <= scores[p] <= 2000
        ]),
        "low": len([p for p in scores if scores[p] < 1500])
    }
    print(f"Score categories: {score_categories}")

    achievement_counts: dict[str, int] = {
        p: len(achievements[p]) for p in achievements
    }
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    unique_players: set[str] = {p for p in scores}
    print(f"Unique players: {unique_players}")

    unique_achievements: set[str] = {
        a for p in achievements for a in achievements[p]
    }
    print(f"Unique achievements: {unique_achievements}")

    active_regions: set[str] = {
        regions[p] for p in regions if p in active_players
    }
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    total_players: int = len(unique_players)
    print(f"Total players: {total_players}")

    total_ach: int = len(unique_achievements)
    print(f"Total unique achievements: {total_ach}")

    avg_score: float = sum(scores[p] for p in scores) / len(scores)
    print(f"Average score: {avg_score}")

    top_player: str = max(scores, key=scores.get)
    top_score: int = scores[top_player]
    top_ach: int = len(achievements[top_player])

    print(
        f"Top performer: {top_player} "
        f"({top_score} points, {top_ach} achievements)"
    )


if __name__ == "__main__":
    main()
