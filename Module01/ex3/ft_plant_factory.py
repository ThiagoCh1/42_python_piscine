class Plant:
    plants = []

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.plants += [self]

    def grow(self) -> None:
        self.height += 1

    def increase_age(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_factory() -> None:
    plant_data = [
        {"name": "Rose", "height": 25, "age": 30},
        {"name": "Oak", "height": 200, "age": 365},
        {"name": "Cactus", "height": 5, "age": 90},
        {"name": "Sunflower", "height": 80, "age": 45},
        {"name": "Fern", "height": 15, "age": 120},
    ]
    for i in plant_data:
        Plant(**i)
    count = 0
    print("=== Plant Factory Output ===")
    for i in Plant.plants:
        print(f"Created: {i.name} ({i.height}cm, {i.age} days)")
        count += 1
    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    ft_plant_factory()
