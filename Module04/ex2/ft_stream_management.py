import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        id = input("Input Stream active. Enter archivist ID: ")
        re = input("Input Stream active. Enter status report: ")
        if not id or not re:
            raise ValueError("Inputs cannot be empty.")
    except ValueError as e:
        sys.stderr.write(f"\n[ERROR] {e}\n")
        return
    sys.stdout.write(f"\n[STANDARD] Archive status from {id}: {re}")
    sys.stderr.write("\n[ALERT] System diagnostic:\
Communication channels verified")
    sys.stdout.write("\n[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
