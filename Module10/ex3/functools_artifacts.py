import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduces a list of spell powers using the specified operation."""
    if not spells:
        return 0

    ops = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min
    }

    if operation not in ops:
        print(f"Error: Unknown operation '{operation}'")
        return 0

    try:
        return functools.reduce(ops[operation], spells)
    except Exception as e:
        print(f"Reducer failed: {e}")
        return 0


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """Creates specialized enchantment functions with pre-filled arguments."""
    try:
        return {
            'fire_enchant': functools.partial(
                base_enchantment, power=50, element='fire'
            ),
            'ice_enchant': functools.partial(
                base_enchantment, power=50, element='ice'
            ),
            'lightning_enchant': functools.partial(
                base_enchantment, power=50, element='lightning'
            )
        }
    except Exception as e:
        print(f"Partial creation failed: {e}")
        return {}


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Calculates Fibonacci numbers efficiently using memoization."""
    if n < 0:
        return 0
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """Returns a single-dispatch function that
    handles different input types."""

    @functools.singledispatch
    def cast(arg):
        return "Unknown spell type"

    @cast.register(int)
    def _(power):
        return f"Casting damage spell with {power} power"

    @cast.register(str)
    def _(enchantment):
        return f"Enchanting with {enchantment}"

    @cast.register(list)
    def _(spells):
        return f"Multi-casting {len(spells)} spells"

    return cast


if __name__ == "__main__":
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    print("\nTesting partial enchanter...")

    def base(power, element, target):
        return f"{element.title()} enchantment (Level {power}) on {target}"

    enchanters = partial_enchanter(base)
    print(enchanters['fire_enchant'](target='Sword'))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(35): {memoized_fibonacci(35)}")

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(100))
    print(cast("Invisibility"))
    print(cast([1, 2, 3]))
