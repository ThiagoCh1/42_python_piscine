def garden_operations():

    print("Testing ValueError...")
    try:
        raise ValueError("abc")
    except ValueError as e:
        print(f"Caught ValueError: invalid literal '{e}' for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        1 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        raise FileNotFoundError("missing.txt")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e}'\n")

    print("Testing KeyError...")
    try:
        data = {"name": "rose", "age": 30}
        data["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together...")
    try:
        data = {"name": "rose", "age": 30}
        data["missing_plant"]
        1 / 0
    except (KeyError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
