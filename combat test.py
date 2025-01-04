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
        while True:  # this loop will continue infinitely until told otherwise ("break" or "return")
            self.displayParty()
            selectedPosition = input("Please select a character by entering a letter: ").strip() # .strip() removes any spaces

            if not selectedPosition: # variables with an inputted value start with the None value. So, if there is no inputted value for selectedPosition, it will have no value and the "not" portion works.
                input("Invalid position selected. Press enter to retry. ") # if selectedPosition has no value, it will tell you.
                os.system("cls")
                continue  # causes the loop to restart without runing any code below.
            
            for hero in heroes:
                if selectedPosition == hero.position:
                    os.system("cls")
                    self.selectedHero = hero
                    moveset.append(list(hero.moveset))
                    return # once enter is pressed, you exit the loop
            
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
        print(moveset)



Aubrey = Hero("Aubrey", 150, 100, ["Shoulder Bash", "Uppercut", "Toss"], "A")
Kelsey = Hero("Kelsey", 85, 125, ["Jab", "Drop Kick"], "B")
Cashmere = Hero("Cashmere", 125, 100, ["Cook", "Whack"], "C")
Omari = Hero("Omari", 100, 150, ["Shoulder Bash", "Study"], "D")
heroes = [Aubrey, Kelsey, Cashmere, Omari]

Slime = Enemy("Slime", 50, {"Goo'd", "Acid Spit"}, "A")
Goblin = Enemy("Goblin", 75, {"Bash"}, "B")
Skeleton = Enemy("Skeleton", 100, {"Slice", "Shoot"}, "C")
enemies = [Slime, Goblin, Skeleton] # once bosses are loaded, append them to this list. old bosses will be removed from the list.

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
            game.displayMoveset()

        Running = False


# create 4 classes: hero, enemy, game, attack
    # the hero class will set the needed parameters to define a character's stats. it will also allow for the selection of characters through the "position" parameter.

    # the enemy class should work similarly to the hero class, down to the selection system.

    # the game class will handle logic. this includes selecting a character to fight with, an enemy to fight, taking & reciving damage, applying debuffs, etc.

    # the attack class will help define specific attacks for characters & weapons.

# the combat should operate like this:
    # while the game is running, ask to select a hero. all of the heroes' stats will be displayed (except moveset).
    # once you select a character, it will then ask you to select an enemy. it will display all of the enemies' stats. below the enemies, it will display your selected hero's name.
    # when a valid enemy position is selected, it will tell you your selected hero & their stats. right below your stats, it will display your selected enemy & their stats. below all of that will be your movelist, and you will be asked to select a move (same positional system as enemy / hero).
    # once the attack is selected, damage will be dealt using a function in the game class. damage dealt is based on the attack.
    # after the attack is preformed, the enemy selects a random action from its moveset and preforms it.
    # repeat until all party members or dead or the enemies are dead.



# gameplay loop:
    # 1. enter a fight
        # 1a. 10 fights total
        # 1b. each fight is a boss
    # 2. after a fight, select one of three random weapons / armor sets OR buffs / "blessings" for each character
        # 2a. these 
    # 3. after every 3 fights, enter a shop

# action class, which can help produce moves that dont deal damage

# 1/3 completed things:
    # short intro cutscene
    # error handling for hero selection
    # error handling for enemy targeting
    # discovered that you can append instances of a class to a list. could be used so that every character shares one movelist.
    # made it so that, after selecting a character & enemy, it will tell you who is attacking who. it will also print the attacker's moveset.
        # this is done by assigning the moveset param for the Hero class a list value.
        # once a valid character is selected, it will append the list of moves to the moveset variable, another list.
        # REMINDER: make it so that, after you select a move & damage is calculated, you remove everything from the list.
