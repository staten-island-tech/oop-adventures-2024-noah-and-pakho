class Hero:
    def __init__(self, name, health, energy, moveset, position):
        self.name = name # str
        self.health = health # int
        self.energy = energy # int
        self.moveset = moveset # list of strings
        self.position = position # string

Aubrey = Hero("Aubrey", 150, 100, ["1", "2", "3"], "A")

moveset = []

moveset.append(list(Aubrey.moveset))

print(moveset)