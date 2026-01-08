def check_temperature(temp_str: str) -> None:
    """
    Check if the provided temperature string is valid and within safe limits.

    Validates that the input is a number and falls within the
    0°C to 40°C range.

    Args:
        temp_str: A string representing the temperature in Celsius.
    """
    print(f"Testing temperature: {temp_str}")
    try:
        temp_val = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return

    if temp_val > 40:
        print(f"Error {temp_val}°C is too hot for plants (max 40°C)\n")
    elif temp_val < 0:
        print(f"Error {temp_val}°C is too cold for plants (min 0°C)\n")
    else:
        print(f"Temperature {temp_val}°C is perfect for plants!\n")


def test_temperature_input() -> None:
    """Run a series of test cases for the temperature checker."""
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
