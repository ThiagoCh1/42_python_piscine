def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("\nAccessing Storage Vault: ancient_fragment.txt")
    try:
        f = open("ancient_fragment.txt", "r")
    except FileNotFoundError:
        print("ERROR:Storage vault not found.")
        return
    print("Connection established...\n")
    print(f.read())
    f.close()
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
