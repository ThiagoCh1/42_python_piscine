def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("\nInitializing new storage unit: new_discovery.txt")
    f = open("new_discovery.txt", "w")
    print("Storage unit created successfully...")
    print("\nInscribing preservation data...")

    text = "{[}ENTRY 001{]} New quantum algorithm discovered\n\
{[}ENTRY 002{]} Efficiency increased by 347%\n\
{[}ENTRY 003{]} Archived by Data Archivist trainee"
    f.write(text)
    print(text)
    print("Data inscription complete. Storage unit sealed")
    f.close()
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
