class Garden:
    def __init__(self, name: str) -> None:
        self.name = name
        self.plants = []

    def add_plant(self, plant) -> None:
        self.plants += [plant]
        print(f"Added {plant.name} to {self.name}'s garden")


class GardenManager:
    gardens = []

    @classmethod
    def create_garden(cls, name: str):
        garden = Garden(name)
        cls.gardens += [garden]
        return garden

    @staticmethod
    def create_garden_network() -> None:
        alice = GardenManager.create_garden("Alice")
        thiago = GardenManager.create_garden("Thiago")

        alice.add_plant(Plant("Oak Tree", 100, 5))
        alice.add_plant(Flowering("Rose", 25, 2, "Red", True))
        alice.add_plant(PrizeFlower("Sunflower", 50, 20, "Yellow", True))
        thiago.add_plant(Plant("Oak", 70, 5))

    @staticmethod
    def new_day() -> None:
        for garden in GardenManager.gardens:
            for plant in garden.plants:
                plant.grow()
                plant.increase_age()
        print("Its a new day, all the plants grew")

    class GardenStats:
        @staticmethod
        def calculate_total_plants(garden) -> None:
            count = 0
            for plant in garden.plants:
                count += 1
            print(f"Total plants in {garden.name}'s garden: {count}")

        @staticmethod
        def average_age(garden) -> None:
            total_age = 0
            count = 0
            average = 0
            for plant in garden.plants:
                total_age += plant.get_age()
                count += 1
            if count != 0:
                average = total_age / count
            print(f"Average age of the garden: {average}")

        @staticmethod
        def plant_types(garden) -> None:
            r = 0
            f = 0
            p = 0
            for plant in garden.plants:
                if plant.plant_type() == "Flowering":
                    f += 1
                elif plant.plant_type() == "Prize":
                    p += 1
                else:
                    r += 1
            print(
                f"Plant types: {r} regular, {f} flowering, "
                f"{p} prize flowers"
            )

        @staticmethod
        def garden_score(garden) -> int:
            total = 0
            for plant in garden.plants:
                if plant.plant_type() == "Prize":
                    total += plant.prize_points
            return total

        @staticmethod
        def total_gardens() -> None:
            count = 0
            for garden in GardenManager.gardens:
                count += 1
            print(f"Total gardens managed: {count}")


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        return self.__height

    def set_height(self, new_height: int) -> None:
        if new_height >= 0:
            self.__height = new_height
        else:
            print(
                f"\nInvalid operation attempted: height "
                f"{new_height}cm [REJECTED]"
            )
            print("Security: Negative height rejected")
            print(
                f"\nCurrent plant: {self.name} ({self.get_height()}cm, "
                f"{self.get_age()} days)"
            )

    def get_age(self) -> int:
        return self.__age

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self.__age = new_age
        else:
            print(
                f"\nInvalid operation attempted: age {new_age} "
                "days [REJECTED]"
            )
            print("Security: Negative age rejected")
            print(
                f"\nCurrent plant: {self.name} ({self.get_height()}cm, "
                f"{self.get_age()} days)"
            )

    def grow(self) -> None:
        self.__height += 1

    def increase_age(self) -> None:
        self.__age += 1

    def plant_type(self) -> str:
        return "Regular"

    def get_info(self) -> None:
        print(
            f"- {self.name} (Regular): {self.get_height()}cm, "
            f"{self.get_age()} days"
        )


class Flowering(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        is_blooming: bool,
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True
        print(f"{self.name} is blooming beautifully!")

    def stop_bloom(self) -> None:
        self.is_blooming = False
        print(f"{self.name} isn't blooming")

    def blooming(self) -> str:
        if self.is_blooming:
            return "Blooming"
        return "Not Blooming"

    def plant_type(self) -> str:
        return "Flowering"

    def get_info(self) -> None:
        print(
            f"- {self.name} (Flowering): {self.get_height()}cm, "
            f"{self.get_age()} days, {self.color} color "
            f"({self.blooming()})"
        )


class PrizeFlower(Flowering):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        is_blooming: bool,
    ) -> None:
        super().__init__(name, height, age, color, is_blooming)
        self.prize_points = self.calculate_prize()

    def calculate_prize(self) -> int:
        points = 0
        if self.is_blooming:
            points += 20
        if self.get_age() <= 30:
            points += 20
        if self.get_height() >= 20:
            points += 20
        return points

    def plant_type(self) -> str:
        return "Prize"

    def get_info(self) -> None:
        print(
            f"- {self.name} (PrizeFlower): {self.get_height()}cm, "
            f"{self.get_age()} days, {self.color} color "
            f"({self.blooming()}), {self.prize_points} points"
        )


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===\n")
    garden_scores = {}
    GardenManager.create_garden_network()
    GardenManager.new_day()
    for garden in GardenManager.gardens:
        print(f"\n=== {garden.name}'s Garden Report ===\n")
        print("Plants in garden:")
        for plant in garden.plants:
            plant.get_info()
        GardenManager.GardenStats.calculate_total_plants(garden)
        GardenManager.GardenStats.average_age(garden)
        GardenManager.GardenStats.plant_types(garden)
        garden_scores[garden] = GardenManager.GardenStats.garden_score(garden)
    formatted_scores = [
        f"{garden.name}: {score}" for garden, score in garden_scores.items()
    ]
    print(f"\nGarden scores - {', '.join(formatted_scores)}")
    GardenManager.GardenStats.total_gardens()


if __name__ == "__main__":
    ft_garden_analytics()
