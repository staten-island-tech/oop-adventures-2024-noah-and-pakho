import os
import json
import random

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
    def __init__(self, name, currentHealth, maxHealth, strength, moveset, position):
        self.name = name
        self.currentHealth = currentHealth
        self.maxHealth = maxHealth
        self.strength = strength
        self.moveset = moveset
        self.position = position
    
    def displayEnemyStats(self): # displays an enemy's stats
        print(f"Name: {self.name}")
        print(f"Health: {self.currentHealth}")
        print(f"Moveset: {self.moveset}")

    def takeTurn(self, heroes):
        targetHero = random.choice(heroes)
        selectedEnemyMove = random.choice(list(self.moveset))

        if selectedEnemyMove:
            print(f"{self.name} uses {selectedEnemyMove} on {targetHero.name}!")
            damage = random.randint(2, 7) * (self.strength / 4)
            targetHero.currentHealth -= damage
            print(f"{self.name} dealt {damage} damage to {targetHero.name}!")
            input("Press Enter to continue. ")

            if targetHero.currentHealth <= 0:
                targetHero.currentHealth = 0
                print(f"{targetHero.name} has been defeated!")
        else:
            print(f"{self.name} has no valid moves to perform.")

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
        while True: 
            self.displayParty()
            selectedPosition = input("Please select a character by entering a letter: ").strip().upper() 
            if not selectedPosition: 
                input("Invalid position selected. Press Enter to retry. ")
                os.system("cls")
                continue
            
            for hero in self.heroes: 
                if selectedPosition == hero.position:
                    if hero.currentHealth <= 0:
                        input(f"{hero.name} is defeated and cannot be selected. Press Enter to retry. ")
                        os.system("cls")
                        continue
                    os.system("cls")
                    self.selectedHero = hero 
                    return 
            input("Invalid position selected. Press enter to retry. ") 
            os.system("cls")
  
    def displayEnemyParty(self):
        os.system("cls")
        aliveEnemies = [enemy for enemy in self.enemies if enemy.currentHealth > 0]
        for enemy in aliveEnemies: # loop that iterates through list of enemies
            print(f"Name: {enemy.name} [{enemy.position}]")
            print(f"Health: {enemy.currentHealth}")
        print(" ")
        print(f"Selected Hero: {self.selectedHero.name}") # reminder that shows your selected hero

    def enemySelect(self):
        os.system("cls")
        print(f"{self.selectedHero.name} is attacking!")
        print("Available enemies to target: ")
        aliveEnemies = [enemy for enemy in self.enemies if enemy.currentHealth > 0]
        for enemy in aliveEnemies:
            print(f"Name: {enemy.name} [{enemy.position}]")
            print(f"Health: {enemy.currentHealth} / {enemy.maxHealth}")
        print("")
        while True:
            selectedEnemyPosition = input("Please target an enemy by entering a letter: ").strip().upper()

            if not selectedEnemyPosition: # same logic present in hero select
                input("Invalid position selected. Press enter to retry. ")
                os.system("cls")
                continue

            for enemy in aliveEnemies:
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
            if selectedMovePosition in positions:
                for move, letter, attack in self.selectedHero.moveset: 
                    if letter == selectedMovePosition and move:
                        return attack
            else:
                input("Invalid move selection. Press Enter to retry. ")
                os.system("cls")

    def combatTurn(self):
        for hero in self.heroes:
            if hero.currentHealth > 0:  
                self.selectedHero = hero
                print(f"{self.selectedHero.name}'s turn:")

                self.enemySelect()  

                if self.selectedEnemy:  
                    selectedMove = self.moveSelect()  
                    os.system("cls")
                    print(f"{self.selectedHero.name} uses {selectedMove} on {self.selectedEnemy.name}!")

                    damage = selectedMove.damage + (self.selectedHero.level * 2)
                    self.selectedEnemy.currentHealth -= damage
                    print(f"{self.selectedHero.name} dealt {damage} damage to {self.selectedEnemy.name}!")
                    input("Press Enter to continue. ")

                    if self.selectedEnemy.currentHealth <= 0:
                        self.selectedEnemy.currentHealth = 0
                        print(f"{self.selectedEnemy.name} has been defeated!")
                        self.selectedEnemy = None  

                if all(enemy.currentHealth <= 0 for enemy in self.enemies):
                    print("All enemies have been defeated!")
                    break  

        if self.selectedEnemy is not None:
            print("\nEnemy's turn!")
            alive_enemies = [enemy for enemy in self.enemies if enemy.currentHealth > 0]

            for enemy in alive_enemies:
                enemy.takeTurn(self.heroes) 

            # Check if all heroes are defeated
            if all(hero.currentHealth == 0 for hero in self.heroes):
                print("All heroes have been defeated! Game Over.")
                input("Press Enter to exit.")
                return

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
testmove = Attack(damage = 999, energyCost = 0, name = "Test")

# characters/heroes
Jade = Hero("Jade", 110, 110, 0, 100, 10, 1, [("Shoulder Bash", "A", shoulderBash), ("Uppercut", "B", uppercut), ("Toss", "C", toss)], "A")
Kelsey = Hero("Kelsey", 80, 80, 0, 90, 8, 1, [("Jab", "A", jab), ("Drop Kick", "B", dropKick)], "B")
Cashmere = Hero("Cashmere", 100, 100, 0, 90, 7, 1, [("Cook", "A", cook), ("Whack", "B", whack)], "C")
Ceres = Hero("Ceres", 90, 90, 0, 50, 8, 1, [("Shoulder Bash", "A", shoulderBash), ("Study", "B", study), ("Test", "C", testmove)], "D")
heroes = [Jade, Kelsey, Cashmere, Ceres]

# enemies
Slime = Enemy("Slime", 25, 25, 50, {"Goo'd", "Acid Spit"}, "A")
Goblin = Enemy("Goblin", 75, 75, 5, {"Bash"}, "B")
Skeleton = Enemy("Skeleton", 100, 100, 10, {"Slice", "Shoot"}, "C")
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
            

# bugs:
    # selecting a hero does not have any effect, as it will always select the first hero in the list.
        # this isnt a bug because there will be no hero select function in the future, it will instead iterate thru the list.
    # when selecting an enemy, it will ask you twice
    # if you select an enemy on the first ask but input an invalid position on the second ask, all of the listed enemies will dissapear.
        # you can still input a valid enemy position & it will select an enemy.
    # after selecting a move, it will quickly flash the damage info before going to the next enemy select
    # loop continues after all enemies / heroes r dead
    # when an enemy is killed, all other enemies do not attack that turn

# things to add:
    # when targeting an enemy, show who you are attacking with

# changes:
    # when selecting an enemy, the hero you are attacking with is displayed.