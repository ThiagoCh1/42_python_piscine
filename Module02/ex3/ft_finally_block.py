def water_plants(plant_list: list[str | None]) -> None:
    """
    Simulate a plant watering process with error handling and cleanup.

    Iterates through a list of plants. If a plant is None, it raises a
    ValueError, but ensures the watering system is closed via a finally block.

    Args:
        plant_list: A list containing plant names (strings) or None.
                    (Note: 'str | None' syntax requires Python 3.10+)
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Run tests for the watering system to demonstrate the finally block."""
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(["tomato", None, "lettuce"])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
