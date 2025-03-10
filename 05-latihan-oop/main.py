class Hero:

    def __init__(self, name: str, health: int, power: int, armor: int) -> None:
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
    
    def attack(self, opponent) -> None:
        print(f"{self.name} attacks {opponent.name}")
        opponent.under_attack(self, self.power)

    def under_attack(self, opponent, amount_attacks) -> None:
        print(f"{self.name} got under attack by {opponent.name}")
        recevied_attacked = amount_attacks / self.armor
        print(f"Recevied damaged: {recevied_attacked}")
        self.health -= recevied_attacked
        print(f"The amount of {self.name}'s health that was left: {self.health}")

# Creating an instance of a class Hero
sniper = Hero("Sniper", 100, 10, 5)
rikimaru = Hero("Rikimaru", 100, 20, 10)

sniper.attack(rikimaru)
print("\n")
rikimaru.attack(sniper)
