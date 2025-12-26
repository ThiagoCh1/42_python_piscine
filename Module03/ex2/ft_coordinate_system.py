import math


def parse_coordinates(coord_str):
    parts = coord_str.split(',')
    position = ()
    i = 0

    while i < len(parts):
        try:
            position = position + (int(parts[i]),)
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            return ()
        i += 1

    return position


def coordinate_system():
    print("=== Game Coordinate System ===")

    origin = (0, 0, 0)
    position = (10, 20, 5)

    print(f"\nPosition created: {position}")
    x1, y1, z1 = origin
    x2, y2, z2 = position
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between {origin} and {position}: {dist:.2f}")

    coord_str = "3,4,0"
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


def main():
    coordinate_system()


if __name__ == "__main__":
    main()
