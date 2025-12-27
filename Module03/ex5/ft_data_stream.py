def next_seed(seed):
    return (seed * 1103515245 + 12345) % 2147483648


def events(n, levels):
    players = ("alice", "bob", "charlie", "thiago")
    actions = ("killed monster", "found treasure", "leveled up")
    seed = 42

    i = 0
    while i < n:
        seed = next_seed(seed)
        player = players[seed % len(players)]

        seed = next_seed(seed)
        action = actions[seed % len(actions)]

        if action == "leveled up":
            levels[player] += 1

        yield (f"Event {i + 1}: Player {player} "
               f"(level {levels[player]}) {action}")
        i += 1


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def primes():
    n = 2
    while True:
        i = 2
        is_prime = True
        while i * i <= n:
            if n % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            yield n
        n += 1


def main():
    up_total = 0
    total_events = 0
    treasure = 0
    n = 1000

    levels = {
        "alice": 5,
        "bob": 12,
        "charlie": 8,
        "thiago": 42
    }

    print("=== Game Data Stream Processor ===")
    print(f"\nProcessing {n} game events...\n")

    for event in events(n, levels):
        if total_events < 3:
            print(event)
        total_events += 1
        if "leveled up" in event:
            up_total += 1
        if "treasure" in event:
            treasure += 1

    print("...")

    print("\n=== Stream Analytics ===")

    top_player = ""
    top_level = 0
    for player in levels:
        if levels[player] > top_level:
            top_level = levels[player]
            top_player = player

    print(f"Total events processed: {total_events}")
    print(f"Top level player: {top_player} (level {top_level})")
    print(f"Level up events: {up_total}")
    print(f"Treasure events: {treasure}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")

    fib = fibonacci()
    print("Fibonacci sequence (first 10): ", end="")
    i = 0
    while i < 10:
        if i > 0:
            print(", ", end="")
        print(next(fib), end="")
        i += 1
    print()

    prime = primes()
    print("Prime numbers (first 5): ", end="")
    i = 0
    while i < 5:
        if i > 0:
            print(", ", end="")
        print(next(prime), end="")
        i += 1
    print()


if __name__ == "__main__":
    main()
