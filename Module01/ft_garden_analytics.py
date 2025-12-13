class Garden:
    gardens = []

    def __init__(self, name):
        self.name = name
        self.plants = []
        Garden.gardens += [self]
    def add_plant(self, plant):
        self.plants += [plant]
        print(f"Added {plant.name} to {self.name}'s garden")
    class Analytics:
        @staticmethod
        def calculate_total_plants():
            count = 0
            for garden in Garden.gardens:
                for plant in garden.plants:
                    count += 1
            print(f"Total plants: {count}")
        @staticmethod
        def average_age(garden):
            total_age = 0
            count = 0
            for plant in garden.plants:
                total_age += plant.age
                count += 1
            average = total_age / count
            print(f"Average age of the garden: {average}")


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
            print(f"\nInvalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
            print(f"\nCurrent plant: {self.name} ({self.get_height()}cm, {self.get_age()} days)")

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print(f"\nInvalid operation attempted: age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")
            print(f"\nCurrent plant: {self.name} ({self.get_height()}cm, {self.get_age()} days)")

    def grow(self):
        self.__height += 1

    def increase_age(self):
        self.__age += 1

class Flower(Plant):
    def __init__(self, name, height, age, color):
          super().__init__(name, height, age)
          self.color = color
    def bloom(self):
            print(f"{self.name} is blooming beautifully!")
    def get_info(self):
        print(f"{self.name} (Flower): {self.get_height()}cm, {self.get_age()} days, {self.color} color")
        self.bloom()

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
          super().__init__(name, height, age)
          self.trunk_diameter = trunk_diameter
    def produce_shade(self):
        shade = (self.trunk_diameter * self.trunk_diameter * 3.14) / 100
        print(f"{self.name} Provides {shade} square meters of shade")
    def get_info(self):
        print(f"{self.name} (Tree): {self.get_height()}cm, {self.get_age()} days, {self.trunk_diameter}cm diameter")
        self.produce_shade()

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    def get_info(self):
        print(f"{self.name} (Vegetable): {self.get_height()}cm, {self.get_age()} days, {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")

