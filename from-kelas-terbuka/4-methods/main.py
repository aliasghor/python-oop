# 4. Python OOP (Object-Oriented Programming) methods

# What is a methods?
# A methods is a function that is defined inside a class; it acts like a behaviour of what the objects can do.

class Hero:
    def __init__(self, name: str, health: int, power: int, armor: int) -> None:
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    # A string method (that returns a string, in this case returns a string representation of an object).
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.name!r}, {self.health!r}, {self.power!r}, {self.armor!r})"
    
    # Void method (a method that doesn't returned anything).
    def who(self) -> None:
        print(f"My name is {self.name}")

    # An void method with parameter
    def attack(self, other: object) -> None:
        print(f"{self.name} attacks {other.name}")



greystone = Hero("Grey Stone",100,30,50)
khaimera = Hero("Khaimera",100,50,30)

print(greystone)
print(khaimera)

greystone.who()

greystone.attack(khaimera)