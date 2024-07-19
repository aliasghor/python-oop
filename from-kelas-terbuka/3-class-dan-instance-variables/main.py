# 3. Python OOP (Object-Oriented Programming) class and instance variabels

# What is the difference between class and instance variables?
# - Instance variables: Instance variables are variables (attributes) that are unique to each instances (objects). Instance variables only exsit inside the __init__ special method, which mean instance variables only defined within the object's attribute not the class it self
# - Class variables: Class variables are variables (attributes) that is shared across all instances (objects). Unlike instance variables, their values are the same for every instances. Class variables (attributes) value are defined within the class and are accessible to all instances.

# An example of class and instance variables:
class Hero:
    # Make a class variable (attribute) that will count how many Hero's object that has been made
    total = 0

    def __init__(self, name: str, health: int) -> None:
        # Make a class instance variables (attributes) that are unique to each instances
        self.name = name
        self.health = health

        # Increment each every Hero's object are made
        Hero.total += 1

hero1 = Hero("Gerry",100)
hero2 = Hero("Mogi",100)

print(hero1.name)
print(hero2.name)

