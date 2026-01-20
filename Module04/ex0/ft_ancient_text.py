def main() -> None:
    """
    Recover and display the contents of the ancient text fragment.

    This function attempts to open the 'ancient_fragment.txt' file,
    reads its contents, and prints them to the standard output to simulate
    a data recovery operation. If the storage vault (file) is not found,
    it displays the specific error message required by the protocol.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("\nAccessing Storage Vault: ancient_fragment.txt")
    try:
        f = open("ancient_fragment.txt", "r")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return
    print("Connection established...")
    print("RECOVERED DATA:")
    print(f.read())
    f.close()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
