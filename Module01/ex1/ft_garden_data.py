class Plant:
    plants = []

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.plants += [self]


def ft_garden_data() -> None:
    Plant("Rose", 25, 30)
    Plant("Sunflower", 80, 45)
    Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    for i in Plant.plants:
        print(f"{i.name}: {i.height}cm, {i.age} days old ")


if __name__ == "__main__":
    ft_garden_data()
