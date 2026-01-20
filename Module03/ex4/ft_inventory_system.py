import sys


def inventory() -> None:
    """
    Manage and analyze an inventory system using strictly authorized methods.
    """
    args: list[str] = sys.argv[1:]
    inventory_dict: dict[str, int] = {}

    for arg in args:
        if ":" not in arg:
            continue
        name: str
        qty_str: str
        name, qty_str = arg.split(":", 1)
        try:
            qty: int = int(qty_str)
        except ValueError:
            continue

        current_qty: int = inventory_dict.get(name, 0)
        inventory_dict.update({name: current_qty + qty})

    print("=== Inventory System Analysis ===")

    total_items: int = 0
    for count in inventory_dict.values():
        total_items += count

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory_dict)}\n")

    print("=== Current Inventory ===")

    items_list: list[tuple[str, int]] = list(inventory_dict.items())
    n: int = len(items_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if items_list[j][1] < items_list[j + 1][1]:
                temp = items_list[j]
                items_list[j] = items_list[j + 1]
                items_list[j + 1] = temp

    for item, quantity in items_list:
        percent: float = 0.0
        if total_items > 0:
            percent = (quantity / total_items) * 100
        print(f"{item}: {quantity} units ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")

    if items_list:
        most_item: str = items_list[0][0]
        most_qty: int = items_list[0][1]
        least_item: str = items_list[-1][0]
        least_qty: int = items_list[-1][1]

        print(f"Most abundant: {most_item} ({most_qty} units)")
        print(f"Least abundant: {least_item} ({least_qty} units)")

    print("\n=== Item Categories ===")
    scarce: dict[str, int] = {}
    moderate: dict[str, int] = {}

    for item, quantity in inventory_dict.items():
        if quantity <= 2:
            scarce.update({item: quantity})
        else:
            moderate.update({item: quantity})

    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock: list[str] = []
    for item, quantity in inventory_dict.items():
        if quantity <= 1:
            restock.append(item)
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory_dict.keys())}")
    print(f"Dictionary values: {list(inventory_dict.values())}")
    print(f"Sample lookup - 'sword' in inventory: "
          f"{'sword' in inventory_dict}")


if __name__ == "__main__":
    inventory()
