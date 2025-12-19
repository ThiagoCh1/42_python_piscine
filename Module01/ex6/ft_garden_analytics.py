class Garden:

    def __init__(self, name):
        self.name = name
        self.plants = []
        GardenManager.gardens += [self]

    def add_plant(self, plant):
        self.plants += [plant]
        print(f"Added {plant.name} to {self.name}'s garden")


class GardenManager:
    gardens = []

    @classmethod
    def create_garden_network(cls):
        alice = Garden("Alice")
        thiago = Garden("Thiago")

        alice.add_plant(Plant("Oak Tree", 100, 5))
        alice.add_plant(Flowering("Rose", 25, 2, "Red", True))
        alice.add_plant(PrizeFlower("Sunflower", 50, 20, "Yellow", True))
        thiago.add_plant(Plant("Oak", 70, 5))

    @staticmethod
    def new_day():
        for garden in GardenManager.gardens:
            for plant in garden.plants:
                plant.grow()
                plant.increase_age()
        print("Its a new day, all the plants grew")

    class GardenStats:
        @staticmethod
        def calculate_total_plants(garden):
            count = 0
            for plant in garden.plants:
                count += 1
            print(f"Total plants in {garden.name}'s garden: {count}")

        @staticmethod
        def average_age(garden):
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
        def plant_types(garden):
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
            print(f"Plant types: {r} regular, {f} flowering, "
                  f"{p} prize flowers")

        @staticmethod
        def garden_score(garden):
            total = 0
            for plant in garden.plants:
                if plant.plant_type() == "Prize":
                    total += plant.prize_points
            return total

        @staticmethod
        def total_gardens():
            count = 0
            for garden in GardenManager.gardens:
                count += 1
            print(f"Total gardens managed: {count}")


class Plant:

    def __init__(self, name, height, age):

        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        return self.__height

    def set_height(self, new_height):
        if new_height >= 0:
            self.__height = new_height
        else:
            text = "\nInvalid operation attempted: " \
                "height {new_height}cm [REJECTED]"
            print(f"{text}")
            print("Security: Negative height rejected")
            print(f"\nCurrent plant: {self.name} ({self.get_height()}cm, "
                  f"{self.get_age()} days)")

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print(f"\nInvalid operation attempted: age {new_age} "
                  "days [REJECTED]")
            print("Security: Negative age rejected")
            print(f"\nCurrent plant: {self.name} ({self.get_height()}cm, "
                  f"{self.get_age()} days)")

    def grow(self):
        self.__height += 1

    def increase_age(self):
        self.__age += 1

    def plant_type(self):
        return ("Regular")

    def get_info(self):
        print(f"{self.name} (Regular): {self.get_height()}cm, "
              f"{self.get_age()} days")


class Flowering(Plant):
    def __init__(self, name, height, age, color, is_blooming):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self):
        self.is_blooming = True
        print(f"{self.name} is blooming beautifully!")

    def stop_bloom(self):
        self.is_blooming = False
        print(f"{self.name} isn't blooming")

    def blooming(self):
        if self.is_blooming:
            return ("Blooming")
        else:
            return ("Not Blooming")

    def plant_type(self):
        return ("Flowering")

    def get_info(self):
        print(f"{self.name} (Flowering): {self.get_height()}cm, "
              f"{self.get_age()} days, {self.color} color "
              f"({self.blooming()})")


class PrizeFlower(Flowering):
    def __init__(self, name, height, age, color, is_blooming):
        super().__init__(name, height, age, color, is_blooming)
        self.prize_points = self.calculate_prize()

    def calculate_prize(self):
        points = 0
        if self.is_blooming:
            points += 20
        if self.get_age() <= 30:
            points += 20
        if self.get_height() >= 20:
            points += 20
        return points

    def plant_type(self):
        return ("Prize")

    def get_info(self):
        print(f"{self.name} (PrizeFlower): {self.get_height()}cm, "
              f"{self.get_age()} days, {self.color} color "
              f"({self.blooming()}), {self.prize_points} points")


def ft_garden_analytics():
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
