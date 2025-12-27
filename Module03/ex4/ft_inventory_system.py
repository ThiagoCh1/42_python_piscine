def inventory():
    print("=== Player Inventory System ===\n")

    inventories = {
        "alice": {
            "sword": {
                "category": "weapon",
                "rarity": "rare",
                "qty": 1,
                "value": 500
            },
            "potion": {
                "category": "consumable",
                "rarity": "common",
                "qty": 5,
                "value": 50
            },
            "shield": {
                "category": "armor",
                "rarity": "uncommon",
                "qty": 1,
                "value": 200
            }
        },
        "bob": {
        }
    }

    total = 0
    i_total = 0
    categories = {}

    print("=== Alice's Inventory ===")
    for item, value in inventories["alice"].items():
        c_total = value["value"] * value["qty"]
        print(f"{item} ({value['category']}, {value['rarity']}): "
              f"{value['qty']}x @ {value['value']} gold each = {c_total} gold")
        total += c_total
        i_total += value["qty"]
        category = value["category"]
        categories[category] = categories.get(category, 0) + value["qty"]

    print(f"Inventory value: {total} gold")
    print(f"Item count: {i_total} items")

    print("Categories: ", end="")
    first = True
    for cat in categories:
        if not first:
            print(", ", end="")
        print(f"{cat}({categories[cat]})", end="")
        first = False
    print()

    print("\n=== Transaction: Alice gives Bob 2 potions ===")

    item = "potion"
    qty = 2

    if inventories["alice"].get(item, {}).get("qty", 0) >= qty:
        inventories["alice"][item]["qty"] -= qty

        if inventories["bob"].get(item):
            inventories["bob"][item]["qty"] += qty
        else:
            inventories["bob"].update({
                item: {
                    "category": inventories["alice"][item]["category"],
                    "rarity": inventories["alice"][item]["rarity"],
                    "qty": qty,
                    "value": inventories["alice"][item]["value"]
                }
            })

        print("Transaction successful!")
    else:
        print("Not enough potions")

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {inventories['alice'].get(item, {}).get('qty', 0)}")
    print(f"Bob potions: {inventories['bob'].get(item, {}).get('qty', 0)}")

    print("\n=== Inventory Analytics ===")

    richest_player = ""
    richest_value = 0
    most_items_player = ""
    most_items_count = 0
    rare_items = {}

    for player in inventories:
        p_value = 0
        p_qty = 0
        for it, val in inventories[player].items():
            p_value += val["value"] * val["qty"]
            p_qty += val["qty"]
            if val.get("rarity") == "rare":
                rare_items[it] = True

        if p_value > richest_value:
            richest_player = player
            richest_value = p_value

        if p_qty > most_items_count:
            most_items_player = player
            most_items_count = p_qty

    print(f"Most valuable player: {richest_player} ({richest_value} gold)")
    print(f"Most items: {most_items_player} ({most_items_count} items)")
    print("Rarest items: ", end="")

    first = True
    for it in rare_items:
        if not first:
            print(", ", end="")
        print(it, end="")
        first = False
    print()


if __name__ == "__main__":
    inventory()
