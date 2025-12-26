import sys


def main():
    args = sys.argv[1:]
    lent = len(args)

    if lent == 0:
        print("=== Player Score Analytics ===")
        print("No scores provided. Usage:"
              " python3 ft_score_analytics.py <score1> <score2> ...")
        return

    i = 0
    while i < lent:
        try:
            args[i] = int(args[i])
        except ValueError:
            print(f"Error: '{args[i]}' is not a valid number")
            return
        i += 1

    print("=== Player Score Analytics ===")
    print(f"Scores processed: {args}")
    print(f"Total players: {lent}")
    print(f"Total score: {sum(args)}")
    print(f"Average score: {sum(args) / lent}")
    print(f"High score: {max(args)}")
    print(f"Low score: {min(args)}")
    print(f"Score range: {max(args) - min(args)}")


if __name__ == "__main__":
    main()
