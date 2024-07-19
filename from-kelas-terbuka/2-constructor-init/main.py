# 2. Python constructor __init__ tutorial

# What is constructor __init__ used for?
# Constructor __init__ is used to initalize an instance's or object's attribute value implicitly using the `self` parameter.
# `self` refers to an object of the class. Currently in this code `self` refers to hero1 and hero2 objects.

# The `class` keyword is used to group every method and attributes together to definew a new type of object (instance). 
class Hero:
    def __init__(self, name: str, health: int, power: int, armor: int) -> None:
        # initialize the object's attribute value to each objects.
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

# Instantiate the instances object
hero1 = Hero("Gerry",100,10,30)
hero2 = Hero("Mogi",100,30,10)

print(hero1.__dict__)
print(hero2.__dict__)