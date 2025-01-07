import os
import json    

class Hero:
    def __init__(self, name, health, energy, moveset, position):
        self.name = name
        self.health = health
        self.energy = energy
        self.moveset = moveset
        self.position = position
    
    def displayStats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Energy: {self.energy}")
        print(f"Moveset: {self.moveset}")

class Enemy:
    def __init__(self, name, health, moveset, position):
        self.name = name
        self.health = health
        self.moveset = moveset
        self.position = position
    
    def displayEnemyStats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Moveset: {self.moveset}")

class Game:
    def __init__(self, heroes):
        self.heroes = heroes
        self.selectedHero = None
        self.selectedEnemy = None
    
    def displayParty(self):
        os.system("cls")
        for hero in heroes:
            print(f"Name: {hero.name} [{hero.position}]")
            print(f"Health: {hero.health} / Energy: {hero.energy}")      
    
    def heroSelect(self):
        while True:
            self.displayParty()
            selectedPosition = input("Please select a character by entering a letter: ").strip()

            if not selectedPosition:
                input("Invalid position selected. Press enter to retry. ")
                os.system("cls")
                continue
            
            for hero in heroes:
                if selectedPosition == hero.position:
                    os.system("cls")
                    self.selectedHero = hero
                    for move in hero.moveset:
                        moveset.append(move)
                    return
            
            input("Invalid position selected. Press enter to retry. ")
            os.system("cls")
  
    def displayEnemyParty(self):
        os.system("cls")
        for enemy in enemies:
            print(f"Name: {enemy.name} [{enemy.position}]")
            print(f"Health: {enemy.health}")
        print(" ")
        print(f"Selected Hero: {self.selectedHero.name}")

    def enemySelect(self):
        while True:
            self.displayEnemyParty()
            selectedEnemyPosition = input("Please target an enemy by entering a letter: ").strip()

            if not selectedEnemyPosition:
                input("Invalid position selected. Press enter to retry. ")
                os.system("cls")
                continue

            for enemy in enemies:
                if selectedEnemyPosition == enemy.position:
                    os.system("cls")
                    self.selectedEnemy = enemy
                    return
            input("Invalid enemy position selected. Press enter to retry. ")
            os.system("cls")
    
    def displayMoveset(self):
        os.system("cls")
        print(f"{self.selectedHero.name} is attacking {self.selectedEnemy.name}!")
        print(" ")
        print(f"{self.selectedHero.name}'s Moveset:")   
        for move, letter in self.selectedHero.moveset:
            if move:
                print(f"{move} [{letter}]")
        print(" ")

    def moveSelect(self):
        while True:
            self.displayMoveset()
            selectedMovePosition = input("Please select a move by entering the letter: ").strip()

            positions = [position for _, position in self.selectedHero.moveset] # this is a "list comprehension", a way to create a new list based on the values of another list.
            # a list comprehension creates a new list of values by iterating over a previously created list.
            # in this case, the list comprehension takes a value from (or unpacks) every tuple in the moveset list, specifically the second one (position).
            # underscores are used when you are unpacking a tuple but want to ignore one of the values.
            if selectedMovePosition in positions: # if the position you selected is in the list of total possible positions:
                for move, position in self.selectedHero.moveset: 
                    if position == selectedMovePosition: # if the second tuple value (position) = the position you picked:
                        return move # this return is here because it will store the selected move in the "selectedMove" variable
            else:
                input("Invalid move selection. Press Enter to retry. ")
                os.system("cls")

    def combatTurn(self):
        selectedMove = self.moveSelect()
        os.system("cls")
        print(f"{self.selectedHero.name} uses {selectedMove} on {self.selectedEnemy.name}!")


# aubrey's moves in her moveset are stored as tuples; one value is the name of the move, and the other is its position.
Aubrey = Hero("Aubrey", 150, 100, [("Shoulder Bash", "A"), ("Uppercut", "B"), ("Toss", "C"), (None, "D")], "A")
Kelsey = Hero("Kelsey", 85, 125, [("Jab", "A"), ("Drop Kick", "B")], "B")
Cashmere = Hero("Cashmere", 125, 100, [("Cook", "A"), ("Whack", "B")], "C")
Omari = Hero("Omari", 100, 150, [("Shoulder Bash", "A"), ("Study", "B")], "D")
heroes = [Aubrey, Kelsey, Cashmere, Omari]

Slime = Enemy("Slime", 50, {"Goo'd", "Acid Spit"}, "A")
Goblin = Enemy("Goblin", 75, {"Bash"}, "B")
Skeleton = Enemy("Skeleton", 100, {"Slice", "Shoot"}, "C")
enemies = [Slime, Goblin, Skeleton]

moveset = []

game = Game(heroes)
    

Running = True

while Running:
    os.system("cls")
    input("Press Enter to start the combat simulation. ")

    game.heroSelect()

    if game.selectedHero:
        game.enemySelect()

        if game.selectedEnemy:
            game.combatTurn()

        Running = False

# how to calculate damage

# how to select a move
    # something like this:
    # the first value in moveset[] has a position = A
    # the second = B
    # etc

# for i in range(moveset):
    # 