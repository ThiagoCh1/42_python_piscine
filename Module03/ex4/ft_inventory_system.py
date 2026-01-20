import sys


def inventory():
    args = sys.argv[1:]
    inventory = {}

    for arg in args:
        if ":" not in arg:
            continue
        name, qty = arg.split(":", 1)
        try:
            qty = int(qty)
        except ValueError:
            continue
        inventory[name] = inventory.get(name, 0) + qty

    print("=== Inventory System Analysis ===")
    total_items = sum(inventory.values())
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}\n")

    print("=== Current Inventory ===")
    for item, qty in sorted(
        inventory.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        percent = (qty / total_items) * 100 if total_items else 0
        print(f"{item}: {qty} units ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most = max(inventory, key=inventory.get)
    least = min(inventory, key=inventory.get)
    print(f"Most abundant: {most} ({inventory[most]} units)")
    print(f"Least abundant: {least} ({inventory[least]} units)")

    print("\n=== Item Categories ===")
    scarce = {}
    moderate = {}

    for item, qty in inventory.items():
        if qty <= 2:
            scarce[item] = qty
        else:
            moderate[item] = qty

    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock = []
    for item, qty in inventory.items():
        if qty <= 1:
            restock.append(item)
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: "
          f"{'sword' in inventory}")


if __name__ == "__main__":
    inventory()
