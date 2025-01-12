import os
import random
import time
currentLevel = 1

class Hero: 
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
    
    def displayStats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.currentHealth} / {self.maxHealth}")
        print(f"Energy: {self.currentEnergy} / {self.maxEnergy}")
        print(f"Moveset: {[move[0] for move in self.moveset]}")

    def regenerateEnergy(self):
        self.currentEnergy += self.energyRegen
        if self.currentEnergy > self.maxEnergy:
            self.currentEnergy = self.maxEnergy


class Enemy: 
    def __init__(self, name, currentHealth, maxHealth, strength, moveset, position):
        self.name = name
        self.currentHealth = currentHealth
        self.maxHealth = maxHealth
        self.strength = strength
        self.moveset = moveset
        self.position = position
    
    def displayEnemyStats(self):
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
            print(f"{self.name} dealt {damage} damage to {targetHero.name}! ({targetHero.currentHealth} / {targetHero.maxHealth})")
            input("Press Enter to continue. ")

            if targetHero.currentHealth <= 0:
                targetHero.currentHealth = 0
                print(f"{targetHero.name} has been defeated!")
        else:
            print(f"{self.name} has no valid moves to perform.")


class Attack:
    def __init__(self, damage, energyCost, name="Unnamed Attack", isHealing = False):
        self.damage = damage
        self.energyCost = energyCost
        self.name = name
        self.isHealing = isHealing

    def __str__(self):
        return self.name


class Game:
    def __init__(self, heroes, enemies):
        self.heroes = heroes
        self.enemies = enemies
        self.selectedHero = None
        self.selectedEnemy = None 

    def displayParty(self):
        os.system("cls")
        for hero in self.heroes:  
            print(f"Name: {hero.name} [{hero.position}]")
            print(f"Health: {hero.currentHealth} / {hero.maxHealth} | Energy: {hero.currentEnergy} / {hero.maxEnergy}")

    def heroSelect(self):
        self.displayParty()
        for hero in self.heroes:
            if hero.currentHealth > 0:
                self.selectedHero = hero
                input("Press Enter to continue. ")
                os.system("cls")
                return

        input("No available heroes. Press Enter to exit.")

    def displayEnemyParty(self):
        os.system("cls")
        aliveEnemies = [enemy for enemy in self.enemies if enemy.currentHealth > 0]
        for enemy in aliveEnemies:
            print(f"Name: {enemy.name} [{enemy.position}]")
            print(f"Health: {enemy.currentHealth}")
        print(" ")
        print(f"Selected Hero: {self.selectedHero.name}") 

    def enemySelect(self):
        os.system("cls")
        aliveEnemies = [enemy for enemy in self.enemies if enemy.currentHealth > 0]
        while True:
            print(f"{self.selectedHero.name} is attacking!")
            print("Available enemies to target: ")
            for enemy in aliveEnemies:
                print(f"Name: {enemy.name} [{enemy.position}]")
                print(f"Health: {enemy.currentHealth} / {enemy.maxHealth}")
            print("")
            selectedEnemyPosition = input("Please target an enemy by entering a letter: ").strip().upper()

            if not selectedEnemyPosition:  
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
        print(f"{self.selectedHero.name} is attacking {self.selectedEnemy.name}!") 
        print(" ")
        print(f"{self.selectedHero.name}'s Moveset:")  
        for move, letter, attack in self.selectedHero.moveset:
            if move:
                if attack.isHealing:
                    if attack.name == "Cook":
                        healingPercentage = 50
                        print(f"{move} [{letter}] (Cost: {attack.energyCost} Energy, Heals: {healingPercentage}% HP)")
                    elif attack.name == "Group Heal":
                        healingPercentage = 20
                        print(f"{move} [{letter}] (Cost: {attack.energyCost} Energy, Heals: {healingPercentage}% of each ally's max HP, and heals slightly less for Cashmere)")
                else:
                    print(f"{move} [{letter}] (Cost: {attack.energyCost} Energy, Damage: {attack.damage})")
        
        if self.selectedHero.currentEnergy == self.selectedHero.maxEnergy:
            print(f"Ultimate Attack [U] - {self.selectedHero.name} unleashes an Ultimate Attack! (Uses all energy)")

        print(" ")

    def moveSelect(self):
        while True:
            self.displayMoveset()
            selectedMovePosition = input("Please select a move by entering the letter: ").strip().upper()

            positions = [letter for _, letter, _ in self.selectedHero.moveset if letter]
            
            if selectedMovePosition in positions:
                for move, letter, attack in self.selectedHero.moveset:
                    if letter == selectedMovePosition and move:
                        if self.selectedHero.currentEnergy >= attack.energyCost: 
                            self.selectedHero.currentEnergy -= attack.energyCost
                            
                            if attack.isHealing:
                                if attack.name == "Group Heal" or attack.name == "Cook":
                                    self.healAlly(attack)
                            return attack
                        else:
                            input("Not enough energy for that attack. Press Enter to retry.")
                            os.system("cls")
            elif selectedMovePosition == 'U' and self.selectedHero.currentEnergy == self.selectedHero.maxEnergy:
                    self.ultimateAttack()
                    return None 
            else:
                    input("Invalid move selection. Press Enter to retry. ")
                    os.system("cls")

    def combatTurn(self):
        for hero in self.heroes:
            if hero.currentHealth > 0:
                self.selectedHero = hero
                print(f"{self.selectedHero.name}'s turn:")

                self.selectedHero.regenerateEnergy()

                self.enemySelect()  

                if self.selectedEnemy:  
                    selectedMove = self.moveSelect() 

                    if selectedMove is None:
                        continue

                    os.system("cls")
                    print(f"{self.selectedHero.name} uses {selectedMove}!")

                    if selectedMove.isHealing:
                        if selectedMove.name == "Group Heal" or selectedMove.name == "Cook":
                            continue  

                    else:
                        damage = selectedMove.damage + (self.selectedHero.level * 2)
                        self.selectedEnemy.currentHealth -= damage
                        print(f"{self.selectedHero.name} dealt {damage} damage to {self.selectedEnemy.name}! ({self.selectedEnemy.currentHealth} / {self.selectedEnemy.maxHealth})")
                        input("Press Enter to continue. ")

                        if self.selectedEnemy.currentHealth <= 0:
                            self.selectedEnemy.currentHealth = 0
                            print(f"{self.selectedEnemy.name} has been defeated!")
                            self.selectedEnemy = None 

                if all(enemy.currentHealth <= 0 for enemy in self.enemies):
                    print("All enemies have been defeated!")
                    break 

        if any(enemy.currentHealth > 0 for enemy in self.enemies):  
            os.system("cls")
            print("Enemy's turn!")
            aliveEnemies = [enemy for enemy in self.enemies if enemy.currentHealth > 0]
            for enemy in aliveEnemies:
                enemy.takeTurn(self.heroes)  

            if all(hero.currentHealth == 0 for hero in self.heroes):
                print("All heroes have been defeated! Game Over.")
                input("Press Enter to exit.")
                return

    def ultimateAttack(self):
        os.system("cls")
        print(f"{self.selectedHero.name} unleashes their Ultimate Attack!")
        ultimateDamage = self.selectedHero.maxEnergy * 2
        if self.selectedEnemy:
            self.selectedEnemy.currentHealth -= ultimateDamage
            print(f"{self.selectedHero.name} dealt {ultimateDamage} damage to {self.selectedEnemy.name}! ({self.selectedEnemy.currentHealth} / {self.selectedEnemy.maxHealth})")
            self.selectedHero.currentEnergy = 0 
        input("Press Enter to continue.")
    
    def healAlly(self, attack):
        availableAllies = [hero for hero in self.heroes if hero.currentHealth > 0]

        if availableAllies:
            if attack.name == "Cook":
                os.system("cls")
                for ally in availableAllies:
                    print(f"{ally.name} [{ally.position}] - Health: {ally.currentHealth} / {ally.maxHealth}")

                allyPosition = input("Enter the position of the ally to heal: ").strip().upper()

                validSelection = False
                for ally in availableAllies:
                    if ally.position == allyPosition:
                        validSelection = True
                        break
                
                if not validSelection:
                    input("Invalid ally position selected. Press Enter to retry.")
                    os.system("cls")
                    return

                for ally in availableAllies:
                    if ally.position == allyPosition:
                        healAmount = ally.maxHealth * 0.50
                        ally.currentHealth += healAmount
                        if ally.currentHealth > ally.maxHealth:  
                            ally.currentHealth = ally.maxHealth
                        os.system("cls")
                        print(f"{self.selectedHero.name} heals {ally.name} for {healAmount:.2f} HP! ({ally.currentHealth} / {ally.maxHealth})")
                        input("Press Enter to continue.")
                        return None
            elif attack.name == "Group Heal":
                os.system("cls")
                for ally in self.heroes:
                    if ally != self.selectedHero:  
                        healAmount = ally.maxHealth * 0.20 
                        ally.currentHealth += healAmount
                        if ally.currentHealth > ally.maxHealth:
                            ally.currentHealth = ally.maxHealth
                        print(f"{self.selectedHero.name} heals {ally.name} for {healAmount:.2f} HP! ({ally.currentHealth} / {ally.maxHealth})")

                if self.selectedHero.name == "Cashmere":
                    healAmount = self.selectedHero.maxHealth * 0.15
                    self.selectedHero.currentHealth += healAmount
                    if self.selectedHero.currentHealth > self.selectedHero.maxHealth:
                        self.selectedHero.currentHealth = self.selectedHero.maxHealth
                    print(f"{self.selectedHero.name} heals himself for {healAmount:.2f} HP! ({self.selectedHero.currentHealth} / {self.selectedHero.maxHealth})")
                input("Press Enter to continue. ")
                return None
        else:
            input("No available allies to heal. Press Enter to continue.")
            os.system("cls")

# moves
shoulderBash = Attack(damage = 17, energyCost=15, name="Shoulder Bash", isHealing = False)
uppercut = Attack(damage = 12, energyCost = 10, name="Uppercut", isHealing = False)
toss = Attack(damage = 20, energyCost = 25, name="Toss", isHealing = False)
jab = Attack(damage = 8, energyCost = 8, name="Jab", isHealing = False)
dropKick = Attack(damage = 13, energyCost = 13, name="Drop Kick", isHealing = False)
whack = Attack(damage = 5, energyCost = 1, name="Whack", isHealing = False)
cook = Attack(damage = 30, energyCost = 15, name="Cook", isHealing = True)
study = Attack(damage = 0, energyCost = 10, name="Study", isHealing = False)
testmove = Attack(damage = 999, energyCost = 0, name="Test", isHealing = False)
basicattack = Attack(damage = 5, energyCost = -17.5, name = "Basic Attack", isHealing = False)
groupheal = Attack(damage = 20, energyCost = 30, name = "Group Heal", isHealing = True)

# characters/heroes
Jade = Hero("Jade", 110, 110, 55, 110, 10, currentLevel, [("Shoulder Bash", "A", shoulderBash), ("Uppercut", "B", uppercut), ("Toss", "C", toss), ("Basic Attack", "D", basicattack)], "A")
Kelsey = Hero("Kelsey", 80, 80, 45, 90, 8, currentLevel, [("Jab", "A", jab), ("Drop Kick", "B", dropKick), ("Basic Attack", "C", basicattack)], "B")
Cashmere = Hero("Cashmere", 100, 100, 45, 90, 7, currentLevel, [("Cook", "A", cook), ("Whack", "B", whack), ("Group Heal", "C", groupheal),("Basic Attack", "D", basicattack)], "C")
Ceres = Hero("Ceres", 90, 90, 50, 50, 8, currentLevel, [("Shoulder Bash", "A", shoulderBash), ("Study", "B", study), ("Test", "C", testmove), ("Basic Attack", "D", basicattack)], "D")
heroes = [Jade, Kelsey, Cashmere, Ceres]

# enemies
Slime = Enemy("Slime", 25, 25, 35, {"Goo'd", "Acid Spit"}, "A")
Goblin = Enemy("Goblin", 75, 75, 12, {"Bash"}, "B")
Skeleton = Enemy("Skeleton", 100, 100, 12, {"Slice", "Shoot"}, "C")
enemies = [Slime, Goblin, Skeleton]

game = Game(heroes, enemies)

randomTip = random.randint(1, 5)
class loop:
    def tips():
        if randomTip == 1:
            displayedTip = "Tip: Your computer is spying on you. Your government is spying on you. No one is safe."
        elif randomTip == 2:
            displayedTip = "Tip: You are never alone. I am in your washing machine every day from 1 AM to 5 AM."
        elif randomTip == 3:
            displayedTip = "Tip: The 'dry' part in the word 'drywall' is a lie. They were not dry."
        elif randomTip == 4:
            displayedTip = "Tip: Every 60 seconds in Africa, a minute goes by everywhere else. This is true!"
        elif randomTip == 5:
            displayedTip = "Tip: Yo'ure mother"
        print(displayedTip)
    def initializeGame():
        os.system("cls")
        print("Loading")
        loop.tips()
        time.sleep(1.5)
        os.system("cls")
        print("Loading .")
        loop.tips()
        time.sleep(1.5)
        os.system("cls")
        print("Loading . .")
        loop.tips()
        time.sleep(1.5)
        os.system("cls")
        print("Loading . . .")
        loop.tips()
        time.sleep(1.5)
        os.system("cls")
        print("Loading . . . .")
        loop.tips()
        time.sleep(1.5)
        os.system("cls")
        print("Loading . . .")
        loop.tips()
        time.sleep(1.5)
        os.system("cls")
        print("Loading . .")
        loop.tips()
        time.sleep(1.5)
        os.system("cls")
        print("Loading .")
        loop.tips()
        time.sleep(1.5)
        os.system("cls")
        input("Done! Press Enter to continue. ")

    def mainLoop():
        while True:
            os.system("cls")
            print("Welcome. Please select an option:")
            print()
            print("[A] - New Game")
            print("[B] - Continue")
            print()
            startingOption = input("Input the letter of the option chosen: ").strip().lower()
            if startingOption not in ["a", "b"]:
                input("Invalid option selected. Press enter to try again. ")
            elif startingOption == "a":
                loop.initializeGame()

                while True:
                    game.heroSelect()

                    if game.selectedHero:
                        game.combatTurn()
            elif startingOption == "b":
                os.system("cls")
                input("Press Enter to start the combat simulation. ")

                while True:
                    game.heroSelect()

                    if game.selectedHero:
                        game.combatTurn()
    def delayPrint(delaySeconds, printString):
        time.sleep(delaySeconds)
        print(printString)

while True:
    os.system("cls")
    print("Welcome. Please select an option:")
    print()
    print("[A] - New Game")
    print("[B] - Continue")
    print()
    startingOption = input("Input the letter of the option chosen: ").strip().lower()
    if startingOption not in ["a", "b"]:
        input("Invalid option selected. Press enter to try again. ")
    elif startingOption == "a":
        loop.initializeGame()
        os.system("cls")
        print("")
        time.sleep(5)
        loop.delayPrint(1.5, "[???] Hello there.")
        loop.delayPrint(1.5, "[???] What are you doing here?")
        loop.delayPrint(1.5, "What...?")
        loop.delayPrint(2, "[???] Who are you? What are you doing here?")
        loop.delayPrint(3, )
        time.sleep(2)
        print("Who are you?")
        playerName = input("Who are you?").strip().lower()
        break

""" 
bugs:
    my will to live

changes:
    when selecting an enemy, the hero you are attacking with is displayed.
    fixed bug where if an invalid enemy position is selected, enemy names / stats won't be printed again.
    made it so that hero health is displayed when enemies deal damage 
    added an onboarding menu

idea:
    one of the characters will be able to generate energy past their max, meaning they have infinite energy.
    one of their moves will be a "wait" move that costs zero energy, but does not deal damage.
    another move will be a move that does damage based on all of your energy past a certain amount
    0 + 1(energy past maxEnergy) * (strength / 5)
    remove all these dumbass comments
"""