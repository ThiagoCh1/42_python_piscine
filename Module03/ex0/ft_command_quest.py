import sys


def main():
    argus = sys.argv
    lent = len(argus)
    print("=== Command Quest ===")
    if lent == 1:
        print("No arguments provided!")
        print(f"Program name: {argus[0]}")
    else:
        i = 1
        print(f"Program name: {argus[0]}")
        print(f"Arguments received: {lent - 1}")
        while i < lent:
            print(f"Argument {i}: {argus[i]}")
            i += 1
    print(f"Total arguments: {lent}")


if __name__ == "__main__":
    main()
