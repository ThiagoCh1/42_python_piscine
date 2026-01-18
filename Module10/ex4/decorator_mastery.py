import time
import functools


def spell_timer(func: callable) -> callable:
    """Decorator that measures and prints execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Spell completed in {end_time - start_time:.3f} seconds")
            return result
        except Exception as e:
            print(f"Timer error: {e}")
            raise e
    return wrapper


def power_validator(min_power: int) -> callable:
    """Decorator factory that validates power level args."""
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power_val = kwargs.get('power')

            if power_val is None:
                for arg in args:
                    if isinstance(arg, int):
                        power_val = arg
                        break
            if power_val is None:
                return "Insufficient power for this spell"

            if power_val >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    """Decorator that retries a function upon failure."""
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return (
                f"Spell casting failed after {max_attempts} attempts"
            )
        return wrapper
    return decorator


class MageGuild:
    """Represents a guild of mages with validation and spell casting."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Validates name: min 3 chars, letters/spaces only."""
        try:
            if not isinstance(name, str):
                return False
            if len(name) < 3:
                return False
            return all(c.isalpha() or c.isspace() for c in name)
        except Exception:
            return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Casts a spell if power is sufficient."""
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting retry spell...")

    @retry_spell(max_attempts=3)
    def broken_spell():
        raise ValueError("Fizzle")

    print(broken_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()

    print(f"Valid 'Merlin': {MageGuild.validate_mage_name('Merlin')}")
    print(f"Valid 'Jo': {MageGuild.validate_mage_name('Jo')}")

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
