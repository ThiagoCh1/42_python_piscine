class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.tank = 2
        self.plants = {}

    def add_plant(self, name, water, sun):
        if name is None:
            raise ValueError("Cannot add None, invalid plant!")
        if name == "":
            raise ValueError("Plant name cannot be empty!")
        if name in self.plants:
            raise PlantError(f"The {name} plant already exists!")
        self.plants[name] = {"water": water, "sun": sun}
        print(f"Added {name} successfully")

    def check_water_tank(self):
        if self.tank <= 0:
            raise WaterError("Not enough water in tank")

    def water_plants(self):
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

    def check_plant_health(self, name):
        if name not in self.plants:
            raise PlantError(f"The {name} plant does not exist!")

        water_level = self.plants[name]["water"]
        sunlight_hours = self.plants[name]["sun"]

        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             " is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             "is too high (max 12)")
        text = f"{name}: healthy (water: {water_level}, sun: {sunlight_hours})"
        return text


def main():
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
