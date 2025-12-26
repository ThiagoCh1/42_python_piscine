class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def trigger_plant_problem():
    raise PlantError("The tomato plant is wilting!")


def trigger_water_problem():
    raise WaterError("Not enough water in the tank!")


def main():
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        trigger_plant_problem()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        trigger_water_problem()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    for func in (trigger_plant_problem, trigger_water_problem):
        try:
            func()
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
