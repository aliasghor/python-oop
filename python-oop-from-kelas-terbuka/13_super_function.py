# super() function is used to give an access to superclass method from the subclass that inherits from it.
# super() function it self returns an object of the superclass's name that then allows us to call the superclass methods from it.

# super() function usage example:

class Hero:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def __repr__(self) -> str:
        return f"{type(self).__name__}('{self.name}', {self.health})"
    
class HeroIntelligent(Hero):
    def __init__(self, name: str) -> None:
        # This is a manual way to access superclass method
        #Hero().__init__(self, name, 100)

        # Access a superclass method init using super() function. Super function it self returns an object of the superclass's name.
        super().__init__(name, 100)

class HeroStrength(Hero):
    def __init__(self, name: str) -> None:
        # Access a superclass method init using super() function. Super function it self returns an object of the superclass's name.
        super().__init__(name, 200)

gerry = HeroIntelligent("Gerry")
mogi = HeroStrength("Mogi")

print(gerry)
print(mogi)