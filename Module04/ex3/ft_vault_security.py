def main() -> None:
    """
    Perform secure file operations using context managers.

    This function simulates a secure vault access by reading from
    'classified_data.txt' and writing to 'security_protocols.txt'
    using the 'with' statement. This ensures files are automatically
    closed (vaults sealed) even if operations fail.
    """
    print("=== CYBER ARCHIVES VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")

    try:
        with open("classified_data.txt", "r") as file:
            print("Vault connection established with failsafe protocols")
            print("\nSECURE EXTRACTION:")
            data = file.read()
            print(data)
    except FileNotFoundError as e:
        print(f"\n[ERROR] {e}")

    with open("security_protocols.txt", "w") as file:
        print("\nSECURE PRESERVATION:")
        text = "[CLASSIFIED] New security protocols archived"
        file.write(text)
        print(text)

    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
