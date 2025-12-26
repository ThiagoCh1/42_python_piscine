def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name is None or plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours}"
                         "  is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")

    try:
        print("\nTesting good values...")
        result = check_plant_health("tomato", 3, 4)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("\nTesting empty plant name...")
        result = check_plant_health("", 3, 4)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("\nTesting bad water level...")
        result = check_plant_health("tomato", 15, 4)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("\nTesting bad sunlight hours...")
        result = check_plant_health("tomato", 3, 0)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
