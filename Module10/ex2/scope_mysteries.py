def mage_counter() -> callable:
    """Returns a function that counts calls. Safe from errors (no args)."""
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    """Returns a function that adds power. Handles non-integer inputs."""
    if not isinstance(initial_power, (int, float)):
        print(f"Warning: Invalid initial power '{initial_power}'. Using 0.")
        initial_power = 0

    total = initial_power

    def accumulate(amount: int):
        nonlocal total
        try:
            total += amount
            return total
        except TypeError:
            return "Error: Power amount must be a number"
    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    """Returns a function that applies an enchantment.
    Validates string input."""
    def enchanter(item_name: str):
        try:
            return f"{enchantment_type} {item_name}"
        except Exception as e:
            return f"Enchantment error: {e}"
    return enchanter


def memory_vault() -> dict:
    """Returns store/recall functions with error
    handling for the dictionary."""
    memory = {}

    def store(key, value):
        try:
            memory[key] = value
            return "Stored"
        except TypeError:

            return "Error: Key must be hashable"

    return {
        'store': store,
        'recall': lambda key: memory.get(key, "Memory not found")
    }


if __name__ == "__main__":
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")

    print("\nTesting spell accumulator (with error)...")
    acc = spell_accumulator(10)
    print(f"Add 5: {acc(5)}")
    print(f"Add 'bad': {acc('bad')}")

    print("\nTesting memory vault (with error)...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print(f"Store Invalid Key: {vault['store'](['list'], 10)}")
    print(f"Recall: {vault['recall']('secret')}")
