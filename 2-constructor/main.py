class Hero:

    def __init__(self, name: str, health: int, power: int, armor: int) -> None:
        # self refers to the class's instance
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    def __repr__(self):
        attrs = ", ".join(f"{key}={value}" for key, value in vars(self).items())
        return f"{type(self).__name__}({attrs})"
    
hero1 = Hero("Gerry", 100, 40, 60)
hero2 = Hero("Mogi", 100, 60, 40)

print(hero1)
print(hero2)