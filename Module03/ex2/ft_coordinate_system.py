import math


def parse_coordinates(coord_str: str) -> tuple:
    """
    Parse a string of coordinates into a tuple of integers.

    Args:
        coord_str: A string containing comma-separated values (e.g., "1,2,3").

    Returns:
        A tuple of integers representing the coordinates. Returns an empty
        tuple if parsing fails.
    """
    parts: list[str] = coord_str.split(',')
    position: tuple = ()
    i: int = 0

    while i < len(parts):
        try:
            position = position + (int(parts[i]),)
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            print(f"Error details Type: {type(e).__name__}, Args: {e.args}")
            return ()
        i += 1

    return position


def coordinate_system() -> None:
    """
    Demonstrate 3D coordinate system operations.

    Creates points, calculates Euclidean distances, parses input strings,
    and demonstrates tuple unpacking.
    """
    print("=== Game Coordinate System ===")

    origin: tuple = (0, 0, 0)
    position: tuple = (10, 20, 5)

    print(f"\nPosition created: {position}")
    x1, y1, z1 = origin
    x2, y2, z2 = position
    dist: float = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between {origin} and {position}: {dist:.2f}")

    coord_str: str = "3,4,0"
    print(f'\nParsing coordinates: "{coord_str}"')
    position = parse_coordinates(coord_str)
    print(f"Parsed position: {position}")
    x2, y2, z2 = position
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between {origin} and {position}: {dist:.2f}")

    coord_str = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{coord_str}"')
    parse_coordinates(coord_str)

    print("\nUnpacking demonstration:")
    print(f"Player at x={x2}, y={y2}, z={z2}")
    print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")


def main() -> None:
    coordinate_system()


if __name__ == "__main__":
    main()
