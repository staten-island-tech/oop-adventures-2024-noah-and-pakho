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
        print(f"Energy: {self.currentEnergy} / {self.maxEnergy}")
        print(f"Moveset: {[move[0] for move in self.moveset]}")

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
    def __init__(self, damage, energyCost, name = "Unnamed Attack"):
        self.damage = damage
        self.energyCost = energyCost
        self.name = name
    def __str__(self):
        return self.name

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
        while True:
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
        for move, letter, attack in self.selectedHero.moveset:
            if move: 
                print(f"{move} [{letter}] (Cost: {attack.energyCost} Energy, Damage: {attack.damage})")
        print(" ")

    def moveSelect(self):
        while True:
            self.displayMoveset()
            selectedMovePosition = input("Please select a move by entering the letter: ").strip().upper()

            positions = [letter for _, letter, _ in self.selectedHero.moveset if letter]
            # the reason why an underscore is where the name value would usually be is because it indicates that the name value is of no use in this situation.
            if selectedMovePosition in positions:
                for move, letter, attack in self.selectedHero.moveset: 
                    if letter == selectedMovePosition and move:
                        return attack # returns the value to where it was originially called to be stored in the selectedMove variable. also breaks out of the loop.
            else:
                input("Invalid move selection. Press Enter to retry. ")
                os.system("cls")

    def combatTurn(self):
        selectedMove = self.moveSelect()
        os.system("cls")
        print(f"{self.selectedHero.name} uses {selectedMove} on {self.selectedEnemy.name}!") # tells you who uses what move on what enemy.
        damage = selectedMove.damage + (self.selectedHero.level * 2)
        self.selectedEnemy.currentHealth -= damage
        print(f"{self.selectedHero.name} dealt {damage} damage to {self.selectedEnemy.name}!")
        if self.selectedEnemy.currentHealth <= 0:
            self.selectedEnemy.currentHealth = 0
            print(f"{self.selectedEnemy.name} has been vanquished...")
            self.selectedEnemy = None
        print(" ")
        input("Press Enter to continue.")

# moves
shoulderBash = Attack(damage = 17, energyCost = 15, name = "Shoulder Bash")
uppercut = Attack(damage = 12, energyCost = 10, name = "Uppercut")
toss = Attack(damage = 20, energyCost = 25, name = "Toss")
jab = Attack(damage=8, energyCost = 8, name = "Jab")
dropKick = Attack(damage = 13, energyCost = 13, name = "Drop Kick")
whack = Attack(damage = 5, energyCost = 1, name = "Whack")
cook = Attack(damage = 1, energyCost = 15, name = "Cook")
study = Attack(damage = 0, energyCost = 10, name = "Study")

# characters/heroes
Jade = Hero("Jade", 110, 110, 0, 100, 10, 1, [("Shoulder Bash", "A", shoulderBash), ("Uppercut", "B", uppercut), ("Toss", "C", toss)], "A")
Kelsey = Hero("Kelsey", 80, 80, 0, 90, 8, 1, [("Jab", "A", jab), ("Drop Kick", "B", dropKick)], "B")
Cashmere = Hero("Cashmere", 100, 100, 0, 90, 7, 1, [("Cook", "A", cook), ("Whack", "B", whack)], "C")
Ceres = Hero("Ceres", 90, 90, 0, 50, 8, 1, [("Shoulder Bash", "A", shoulderBash), ("Study", "B", study)], "D")
heroes = [Jade, Kelsey, Cashmere, Ceres]

# enemies
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
            

# common patterns in code:
    # treating None values like False values
    # creating infinite loops that are used for error handling