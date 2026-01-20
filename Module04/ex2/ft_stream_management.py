import sys


def main() -> None:
    """
    Manage input and output using standard and alert data streams.

    This function prompts the user for an archivist ID and a status
    report via the standard input. It routes the data to the appropriate
    streams: standard messages to sys.stdout and system alerts to
    sys.stderr.
    """
    print("CYBER ARCHIVES")
    print("COMMUNICATION SYSTEM")

    arch_id = input("Input Stream active. Enter archivist ID: ")
    report = input("Input Stream active. Enter status report: ")

    if not arch_id or not report:
        sys.stderr.write("[ERROR] Inputs cannot be empty.\n")
        return

    msg = f"[STANDARD] Archive status from {arch_id}: {report}\n"
    sys.stdout.write(msg)
    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n"
    )
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
