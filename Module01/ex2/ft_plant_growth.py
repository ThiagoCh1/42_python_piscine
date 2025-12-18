class Plant:
    plants = []

    def __init__(self, name, height, age):

        self.name = name
        self.height = height
        self.age = age
        Plant.plants += [self]

    def grow(self):
        self.height += 1

    def increase_age(self):
        self.age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth():
    Plant("Rose", 25, 30)
    Plant("Sunflower", 80, 45)
    start_h = {}
    time = 7
    print("=== Day 1 ===")
    for i in Plant.plants:
        i.get_info()
        start_h[i] = i.height
    for i in Plant.plants:
        day = 1
        while day < time:
            i.grow()
            i.increase_age()
            day += 1
    print(f"=== Day {time} ===")
    for i in Plant.plants:
        i.get_info()
        growth = i.height - start_h[i]
        print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
