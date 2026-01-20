import sys


def main() -> None:
    """
    This function retrieves command-line arguments via sys.argv, determines
    the number of arguments, and prints them in a specific format as required
    by the exercise. It handles cases with no arguments provided and lists
    individual arguments when present.
    """
    argus: list[str] = sys.argv
    lent: int = len(argus)

    print("=== Command Quest ===")

    if lent == 1:
        print("No arguments provided!")
        print(f"Program name: {argus[0]}")
    else:
        i: int = 1
        print(f"Program name: {argus[0]}")
        print(f"Arguments received: {lent - 1}")
        while i < lent:
            print(f"Argument {i}: {argus[i]}")
            i += 1

    print(f"Total arguments: {lent}")


if __name__ == "__main__":
    main()
