import os
import json    

class Hero: # class for your characters
    def __init__(self, name, currentHealth, maxHealth, currentEnergy, maxEnergy, energyRegen, level, moveset, position):
        self.name = name
        self.currentHealth = currentHealth
        self.maxHealth = maxHealth
        self.currentEnergy = currentEnergy
        self.maxEnergy = maxEnergy
        self.energyRegen = energyRegen
        self.level = level
        self.moveset = moveset
        self.position = position
    
    def displayStats(self): # displays a character's stats
        print(f"Name: {self.name}")
        print(f"Health: {self.currentHealth} / {self.maxHealth}")
        print(f"Energy: {self.energy}")
        print(f"Moveset: {self.moveset}")

class Enemy: # a class for enemies you fight against
    def __init__(self, name, currentHealth, maxHealth, moveset, position):
        self.name = name
        self.currentHealth = currentHealth
        self.maxHealth = maxHealth
        self.moveset = moveset
        self.position = position
    
    def displayEnemyStats(self): # displays an enemy's stats
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Moveset: {self.moveset}")

class Attack:
    def __init__(self, damage, energyCost):
        self.damage = damage
        self.energyCost = energyCost
        

class Game:
    def __init__(self, heroes, enemies): # every instance of game will already have the list of heroes & enemies.
        self.heroes = heroes
        self.enemies = enemies
        self.selectedHero = None 
        self.selectedEnemy = None # this & the above lines are used for functions below.
    
    def displayParty(self):
        os.system("cls")
        for hero in self.heroes: # loop that iterates through the list of heroes and displays each hero's stats
            print(f"Name: {hero.name} [{hero.position}]")
            print(f"Health: {hero.currentHealth} / Energy: {hero.currentEnergy}")      
    
    def heroSelect(self):
        while True: # used to create an infinite loop. while in this loop, you are repeatedly asked to select a hero. the loop is only broken when you select a valid position.
            self.displayParty()
            selectedPosition = input("Please select a character by entering a letter: ").strip().upper() # .strip() is used to get rid of whitespace / unnecessary spaces.
            if not selectedPosition: # if an input is given no value to assign to a function, it defaults to None. this detects if selectedPosition has a value; if not, then it will assume you didn't enter a valid position and will prompt you to retry.
                input("Invalid position selected. Press Enter to retry. ")
                os.system("cls")
                continue # allows the infinite loop to continue.
            
            for hero in self.heroes: # if any value is given to selectedPosition, it skips over the empty value check and comes here.
                if selectedPosition == hero.position: # checks if selectedPosition is the same as ANY hero's position
                    os.system("cls")
                    self.selectedHero = hero # sets the hero with the corresponding position to the value of selectedHero
                    return # breaks the loop, allowing for the next game function to run
            input("Invalid position selected. Press enter to retry. ") # if selectedPosition has a value but is NOT a valid position, it comes here. once input is given, the loop restarts itself.
            os.system("cls") # this bit of code is outside fo the for loop because you only want this to show up after checking every hero.
  
    def displayEnemyParty(self):
        os.system("cls")
        for enemy in self.enemies: # loop that iterates through list of enemies
            print(f"Name: {enemy.name} [{enemy.position}]")
            print(f"Health: {enemy.currentHealth}")
        print(" ")
        print(f"Selected Hero: {self.selectedHero.name}") # reminder that shows your selected hero

    def enemySelect(self):
        while True: # same loop in hero select
            self.displayEnemyParty()
            selectedEnemyPosition = input("Please target an enemy by entering a letter: ").strip().upper()

            if not selectedEnemyPosition: # same logic present in hero select
                input("Invalid position selected. Press enter to retry. ")
                os.system("cls")
                continue

            for enemy in self.enemies:
                if selectedEnemyPosition == enemy.position:
                    os.system("cls")
                    self.selectedEnemy = enemy
                    return
            input("Invalid enemy position selected. Press enter to retry. ")
            os.system("cls")
    
    def displayMoveset(self):
        os.system("cls")
        print(f"{self.selectedHero.name} is attacking {self.selectedEnemy.name}!") # tells you which hero is attacking which enemy
        print(" ")
        print(f"{self.selectedHero.name}'s Moveset:")  # reminder of who's moveset you're looking at 
        for move, letter in self.selectedHero.moveset: # this for loop is a special kind of loop only for unpacking tuples (or iterating over a list of tuples). move will be the first value in the tuple (name), and letter will be the second value (position).
            if move: # movesets will have a maximum size of 4 moves, but a character wont always have exactly 4 moves. empty move slots will have "None" as the name value. this if statement checks if a move has a None value or not; if it does, it wont print its name.
                print(f"{move} [{letter}]")
        print(" ")

    def moveSelect(self):
        while True: # same loop in hero select
            self.displayMoveset()
            selectedMovePosition = input("Please select a move by entering the letter: ").strip().upper()

            positions = [position for _, position in self.selectedHero.moveset] # this is called list comprehension. it's a for loop that unpacks the tuples in the selected hero's moveset and puts the second tuple value (position) into the list for later use.
            # the reason why an underscore is where the name value would usually be is because it indicates that the name value is of no use in this situation.
            if selectedMovePosition in positions:
                for move, position in self.selectedHero.moveset: 
                    if position == selectedMovePosition:
                        return move # returns the value to where it was originially called to be stored in the selectedMove variable. also breaks out of the loop.
            else:
                input("Invalid move selection. Press Enter to retry. ")
                os.system("cls")

    def combatTurn(self):
        selectedMove = self.moveSelect()
        os.system("cls")
        print(f"{self.selectedHero.name} uses {selectedMove} on {self.selectedEnemy.name}!") # tells you who uses what move on what enemy.
        # logic for calculating damage will go here
        print(f"{self.selectedHero.name} dealt 0 damage to {self.selectedEnemy.name}!")
        print(" ")
        input("Press Enter to continue.")
Jade = Hero("Jade", 110, 110, 0, 100, 10, 1, [("Shoulder Bash", "A"), ("Uppercut", "B"), ("Toss", "C"), (None, "D")], "A")
Kelsey = Hero("Kelsey", 80, 80, 0, 90, 8, 1, [("Jab", "A"), ("Drop Kick", "B")], "B")
Cashmere = Hero("Cashmere", 100, 100, 0, 90, 7, 1, [("Cook", "A"), ("Whack", "B")], "C")
Ceres = Hero("Ceres", 90, 90, 0, 50, 8, 1, [("Shoulder Bash", "A"), ("Study", "B")], "D")
"""Jade = Hero("Jade", 150, 100, 1, [("Shoulder Bash", "A"), ("Uppercut", "B"), ("Toss", "C"), (None, "D")], "A")
Kelsey = Hero("Kelsey", 85, 125, 1, [("Jab", "A"), ("Drop Kick", "B")], "B")
Cashmere = Hero("Cashmere", 125, 100, 1, [("Cook", "A"), ("Whack", "B")], "C")
Ceres = Hero("Ceres", 100, 150, 1, [("Shoulder Bash", "A"), ("Study", "B")], "D")"""
heroes = [Jade, Kelsey, Cashmere, Ceres]

Slime = Enemy("Slime", 50, 50,{"Goo'd", "Acid Spit"}, "A")
Goblin = Enemy("Goblin", 75, 75, {"Bash"}, "B")
Skeleton = Enemy("Skeleton", 100, 100, {"Slice", "Shoot"}, "C")
enemies = [Slime, Goblin, Skeleton]

game = Game(heroes, enemies)

os.system("cls")
input("Press Enter to start the combat simulation. ")

while True:
    game.heroSelect()

    if game.selectedHero:
        game.enemySelect()

        if game.selectedEnemy:
            game.combatTurn()
            break
            

# common patterns in code:
    # treating None values like False values
    # creating infinite loops that are used for error handling