class GardenError(Exception):
    """Base class for all garden-related exceptions."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-specific issues (e.g., duplicates)."""
    pass


class WaterError(GardenError):
    """Exception raised for water-supply issues."""
    pass


class GardenManager:
    """
    Manages a collection of plants and a water tank resource.

    Attributes:
        tank (int): Current water units available in the tank.
        plants (dict): Dictionary storing plant data keyed by plant name.
    """

    def __init__(self) -> None:
        """Initialize the garden with a default water tank and empty plants."""
        self.tank: int = 2
        self.plants: dict[str, dict[str, int]] = {}

    def add_plant(self, name: str | None, water: int, sun: int) -> None:
        """
        Add a new plant to the garden inventory.

        Args:
            name: The name of the plant. Cannot be empty or None.
            water: Initial water level (integer).
            sun: Sunlight hours (integer).

        Raises:
            ValueError: If the name is None or an empty string.
            PlantError: If a plant with this name already exists.
        """
        if name is None:
            raise ValueError("Cannot add None, invalid plant!")
        if name == "":
            raise ValueError("Plant name cannot be empty!")
        if name in self.plants:
            raise PlantError(f"The {name} plant already exists!")

        self.plants[name] = {"water": water, "sun": sun}
        print(f"Added {name} successfully")

    def check_water_tank(self) -> None:
        """
        Verify if the water tank has sufficient resources.

        Raises:
            WaterError: If the tank is empty or negative.
        """
        if self.tank <= 0:
            raise WaterError("Not enough water in tank")

    def water_plants(self) -> None:
        """
        Attempt to water all plants in the garden.

        Iterates through plants and consumes tank resources. Handles specific
        WaterErrors per plant allowing the loop to continue, while ensuring
        system cleanup via a finally block.
        """
        print("Opening watering system")
        try:
            for plant, data in self.plants.items():
                try:
                    self.check_water_tank()

                    if data["water"] > 9:
                        raise WaterError("Too much water in the plant!")

                    data["water"] += 1
                    self.tank -= 1
                    print(f"Watering {plant} - success")

                except WaterError as e:
                    print(f"Error watering {plant}: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name: str) -> str:
        """
        Assess the health of a specific plant based on its stats.

        Args:
            name: The name of the plant to check.

        Returns:
            A string summary of the plant's health.

        Raises:
            PlantError: If the plant is not in the garden.
            ValueError: If water or sun levels are out of safe bounds.
        """
        if name not in self.plants:
            raise PlantError(f"The {name} plant does not exist!")

        water_level = self.plants[name]["water"]
        sunlight_hours = self.plants[name]["sun"]

        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        if sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )

        return (
            f"{name}: healthy "
            f"(water: {water_level}, sun: {sunlight_hours})"
        )


def main() -> None:
    """Run the main simulation of the Garden Management System."""
    print("=== Garden Management System ===")

    garden = GardenManager()

    print("\nAdding plants to garden...")
    plants_to_add = [
        ("tomato", 5, 8),
        ("lettuce", 15, 8),
        ("", 5, 8),
        ("tomato", 5, 8),
    ]

    for name, water, sun in plants_to_add:
        try:
            garden.add_plant(name, water, sun)
        except (GardenError, ValueError) as e:
            print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    garden.water_plants()

    print("\nChecking plant health...")
    plants_to_check = ["tomato", "lettuce", "ghost"]

    for name in plants_to_check:
        try:
            print(garden.check_plant_health(name))
        except (GardenError, ValueError) as e:
            print(f"Error Checking {name}: {e}")

    print("\nTesting error recovery...")
    try:
        garden.check_water_tank()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    main()
