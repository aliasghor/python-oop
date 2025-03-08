# Creating a template for the Hero's instance / object
class Hero:
    pass

# Creating instances of the Hero class
gerry = Hero()
mogi = Hero()

gerry.name = "Gerry"
gerry.health = 100

mogi.name = "Gerry"
mogi.health = 100


print(f"Hero's name: {gerry.name}\nHero's health: {gerry.health}")
print(f"Hero's name: {mogi.name}\nHero's health: {mogi.health}")