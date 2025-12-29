class Plant:
    plants = []

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.plants += [self]

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        print(
            f"{self.name} (Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color"
        )
        self.bloom()


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int,
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = (self.trunk_diameter * self.trunk_diameter * 3.14) / 100
        print(f"{self.name} Provides {shade} square meters of shade")

    def get_info(self) -> None:
        print(
            f"{self.name} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )
        self.produce_shade()


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        print(
            f"{self.name} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
        )
        print(f"{self.name} is rich in {self.nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    Flower("Rose", 25, 30, "red")
    Flower("Daisy", 12, 14, "white")

    Tree("Oak", 500, 1825, 50)
    Tree("Maple", 350, 1000, 30)

    Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    Vegetable("Carrot", 20, 45, "winter", "vitamin A")

    for i in Plant.plants:
        print()
        i.get_info()


if __name__ == "__main__":
    ft_plant_types()
