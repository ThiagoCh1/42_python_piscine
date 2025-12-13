class SecurePlant:
    plants = {}

    def __init__(self, name, height, age):

        self.name = name
        print(f"Plant created: {name}")
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)
        SecurePlant.plants[self.name] = self

    def get_height(self):
        return self.__height

    def set_height(self, new_height):
        if new_height >= 0:
            self.__height = new_height
            print(f"Height updated: {new_height}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
            print(f"\nCurrent plant: {self.name} ({self.get_height()}cm, {self.get_age()} days)")

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
            print(f"Age updated: {new_age} days [OK]")
        else:
            print(f"\nInvalid operation attempted: age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")
            print(f"\nCurrent plant: {self.name} ({self.get_height()}cm, {self.get_age()} days)")

    def grow(self):
        self.__height += 1

    def increase_age(self):
        self.__age += 1

    def get_info(self):
        print(f"{self.name}: {self.__height}cm, {self.__age} days old")

def ft_garden_security():
    print("=== Garden Security System ===")
    SecurePlant("Rose", 25, 30)
    SecurePlant.plants["Rose"].set_height(-5)

if __name__ == "__main__":
    ft_garden_security()
