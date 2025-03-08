class FloweringPlants:
    # Class variable is shared across all instances of a class
    species = "Asteraceae"

    def __init__(self, name: str, location: str):
        # Instance variables are unique to each instance of a class
        self.name = name
        self.location = location

    def __repr__(self):
        attrs = ", ".join(f"{key}={value}" for key, value in vars(self).items())
        return f"{type(self).__name__}({attrs})"
    
sunflower = FloweringPlants("Sunflower", "North and South America")
arnica = FloweringPlants("Arnica", "North America")

print(sunflower)
print(arnica)

print(f"Plants species name: {sunflower.species}")
print(f"Plants species name: {arnica.species}")