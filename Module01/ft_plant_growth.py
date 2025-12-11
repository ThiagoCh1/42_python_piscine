class Plant:
    plants = []

    def __init__(self, name, height, age):

        self.name = name
        self.height = height
        self.age = age
        Plant.plants.append(self)

    def grow(self):
        self.height += 1

    def incriase_age(self):
        self.age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth():
    Plant("Rose", 25, 30)
    Plant("Sunflower", 80, 45)
    start_h = {}
    print("=== Day 1 ===")
    for i in Plant.plants:
        Plant.get_info(i)
        start_h[i] = i.height
    for i in Plant.plants:
        day = 1
        while day < 7:
            i.grow()
            i.incriase_age()
            day += 1
    print("=== Day 7 ===")
    for i in Plant.plants:
        Plant.get_info(i)
        growth = i.height - start_h[i]
        print(f"Growth this week: +{growth}cm")


ft_plant_growth()
