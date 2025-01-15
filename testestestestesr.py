import os
import random
import time
import inShop

global currentLevel
currentLevel = 1
global currentLevelUltimateModifier
currentLevelUltimateModifier = 0.75
playerName = ""
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
    
    def __str__(self):
        return f"{self.name}, {self.moveset}"

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

        if selectedEnemyMove == "Roll Over":
            self.rollOverAttack(heroes)
            input("Press Enter to continue. ")
        elif selectedEnemyMove == "String Shot":
            self.stringShotAttack(heroes)
            input("Press Enter to continue. ")
        elif selectedEnemyMove == "Blood Ichor":
            self.bloodIchor(heroes)
            input("Press Enter to continue. ")
        elif selectedEnemyMove == "Noxious Shot":
            self.noxiousShot(heroes)
            input("Press Enter to continue. ")
        else:
            if selectedEnemyMove:
                print(f"{self.name} uses {selectedEnemyMove} on {targetHero.name}!")
                damage = random.randint(2, 7) * (self.strength / 4)
                targetHero.currentHealth -= damage
                print(f"{self.name} dealt {damage} damage to {targetHero.name}! ({targetHero.currentHealth} / {targetHero.maxHealth})")
                input("Press Enter to continue. ")

                if targetHero.currentHealth <= 0:
                    targetHero.currentHealth = 0
                    os.system("cls")
                    print(f"{targetHero.name} has been defeated!")
            else:
                print(f"{self.name} has no valid moves to perform.")
    def rollOverAttack(self, heroes):
        print(f"{self.name} uses Roll Over! ")
        totalDmg = 15
        for hero in heroes:
            if hero.currentHealth > 0:
                hero.currentHealth -= totalDmg
                if hero.currentHealth < 0:
                    hero.currentHealth = 0
                print(f"{self.name} dealt {totalDmg} damage to {hero.name}! ({hero.name} now has {hero.currentHealth} health!)")
    def stringShotAttack(self, heroes):
        print(f"{self.name} uses String Shot! ")
        totalDmg = 15
        for hero in heroes:
            if hero.currentHealth > 0:
                hero.currentHealth -= totalDmg
                if hero.currentHealth < 0:
                    hero.currentHealth = 0
                print(f"{self.name} dealt {totalDmg} damage to {hero.name}! ({hero.name} now has {hero.currentHealth} health!)")
    def bloodIchor(self, heroes):
        targetHero = random.choice(heroes)
        print(f"{self.name} uses Blood Ichor!")
        totalDmg = 5
        if targetHero.currentHealth > 0:
            targetHero.currentHealth -= totalDmg
            self.currentHealth += 10
            if targetHero.currentHealth < 0:
                targetHero.currentHealth = 0
            print(f"{self.name} dealt {totalDmg} damage to {targetHero}! {self.name} healed 10 health! ({targetHero.name} now has {targetHero.currentHealth} health!)")
        input("Press Enter to continue. ")
    def noxiousShot(self, heroes):
        print(f"{self.name} uses Noxious Shot!")
        totalDmg = 2 * self.strength
        for hero in heroes:
            if hero.currentHealth > 0:
                hero.currentHealth -= totalDmg
                if hero.currentHealth < 0:
                    hero.currentHealth = 0
                print(f"{self.name} dealt {totalDmg} damage to {hero.name}! ({hero.name} now has {hero.currentHealth} health!)")
    def bloodHarvest(self, heroes):
        targetHero = random.choice(heroes)
        print(f"{self.name} uses Blood Harvest!")
        totalDmg = 30
        if targetHero.currentHealth > 0:
            targetHero.currentHealth -= totalDmg
            self.currentHealth += 25
            if targetHero.currentHealth < 0:
                targetHero.currentHealth = 0
            print(f"{self.name} dealt {totalDmg} damage to {targetHero}! {self.name} healed 10 health! ({targetHero.name} now has {targetHero.currentHealth} health!)")

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
            if hero.currentEnergy > hero.maxEnergy:
                hero.currentEnergy = hero.maxEnergy
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

        input("No available heroes. Press Enter to exit. ")

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
            print(f"{self.selectedHero.name} ({self.selectedHero.currentHealth} / {self.selectedHero.maxHealth} Health, {self.selectedHero.currentEnergy} / {self.selectedHero.maxEnergy} Energy)")
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
        print(f"{self.selectedHero.name}: ({self.selectedHero.currentHealth} / {self.selectedHero.maxHealth} Health, {self.selectedHero.currentEnergy} / {self.selectedHero.maxEnergy} Energy)")
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

                aliveEnemies = [enemy for enemy in self.enemies if enemy.currentHealth > 0]
                if not aliveEnemies:
                    os.system("cls")
                    print("All enemies have been defeated!")
                    input("Press Enter to continue. ")
                    return False  

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
                        input("Press Enter to continue.")

                        if self.selectedEnemy.currentHealth <= 0:
                            self.selectedEnemy.currentHealth = 0
                            print(f"{self.selectedEnemy.name} has been defeated!")
                            self.selectedEnemy = None  

                   
                    if all(enemy.currentHealth <= 0 for enemy in self.enemies):
                        os.system("cls")
                        print("All enemies have been defeated!")
                        input("Press Enter to continue. ")
                        return False  

        
        if any(enemy.currentHealth > 0 for enemy in self.enemies):
            os.system("cls")
            print("Enemy's turn!")
            aliveEnemies = [enemy for enemy in self.enemies if enemy.currentHealth > 0]
            for enemy in aliveEnemies:
                enemy.takeTurn(self.heroes)

            
            if all(hero.currentHealth == 0 for hero in self.heroes):
                print("All heroes have been defeated! Game Over.")
                input("Press Enter to exit. ")
                return False 
        return True 
                

    def ultimateAttack(self):
        os.system("cls")
        print(f"{self.selectedHero.name} unleashes their Ultimate Attack!")
        global currentLevelUltimateModifier
        ultimateDamage = self.selectedHero.maxEnergy * currentLevelUltimateModifier
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

class loop:
    def tips():
        randomTip = random.randint(1, 11)
        if randomTip == 1 or randomTip == 2:
            displayedTip = "Tip: Your computer is spying on you. Your government is spying on you. No one is safe."
        elif randomTip == 3 or randomTip == 4:
            displayedTip = "Tip: You are never alone. I am in your washing machine every day from 1 AM to 5 AM."
        elif randomTip == 5 or randomTip == 6:
            displayedTip = "Tip: The 'dry' part in the word 'drywall' is a lie. It was not dry."
        elif randomTip == 7 or randomTip == 8:
            displayedTip = "Tip: Every 60 seconds in Africa, a minute goes by everywhere else. This is true!"
        elif randomTip == 9 or randomTip == 10:
            displayedTip = "Tip: There is a secret code that activates easy mode!"
        elif randomTip == 11:
            displayedTip = "Tip: This project is brought to you by a poorly designed garble of spaghetti code. Please do not test its limits or it will cry. And then I will cry. "
        print(displayedTip)
    def loadingScreen():
        os.system("cls")
        print("Loading . . . ")
        loop.tips()
        time.sleep(3.5)
        input("Done! Press Enter to continue. ")

    def mainLoop():
        while True:
            os.system("cls")
            print("Welcome. Please select an option:")
            print()
            print("[A] - New Game")
            print()
            startingOption = input("Input the letter of the option chosen: ").strip().lower()
            if startingOption not in ["a"]:
                input("Invalid option selected. Press enter to try again. ")
            elif startingOption == "a":
                break
        
        loop.loadingScreen()
        os.system("cls")
        
        global playerName
        yes = True
        while yes:
            playerName = input("Who are you? ").strip()
            if playerName == "":
                input("[???] Sorry, I didn't get that. Come again? ")
                os.system("cls")
            else:
                loop.delayPrint(1, f"I am {playerName}.")
                yes = False
                confirm = input(f"Your name is {playerName}? Y/N ")
                if confirm not in ["y", "yes", "n", "no"]:
                    input("Invalid input. Try again. ")
                elif confirm in ["y", "yes"]:
                    break
                elif confirm in ["n", "no"]:
                    yes = True
        time.sleep(2)
        # moves
        basicattack = Attack(damage = 5, energyCost = -17.5, name = "Basic Attack", isHealing = False)
        sliceattack = Attack(damage = 10, energyCost = 10, name = "Slice", isHealing = False)

        # characters/heroes
        global currentLevel
        Ceres = Hero(playerName, 90, 90, 45, 90, 5, currentLevel, [("Basic Attack", "A", basicattack), ("Slice", "B", sliceattack)], "A")
        heroes = [Ceres]

        os.system("cls")
        
        headbutt = Attack(15, 10, "Headbutt", isHealing = False)
        slam = Attack(10, 5, "Slam", isHealing = False)
        cook = Attack(50, 17.5, "Cook", isHealing = True)

        Ceres.currentHealth = 90
        Ceres.currentEnergy = 45
        Jade = Hero("Jade", 120, 120, 50, 100, 2.5, currentLevel, [("Basic Attack", "A", basicattack), ("Headbutt", "B", headbutt)], "B")
        Kelsey = Hero("Kelsey", 75, 75, 55, 110, 10, currentLevel, [("Basic Attack", "A", basicattack), ("Slam", "B", slam)], "C")
        Cashmere = Hero("Cashmere", 140, 140, 75, 150, 5, currentLevel, [("Basic Attack", "A", basicattack), ("Cook", "B", cook)], "D")
        heroes.append(Jade)
        heroes.append(Kelsey)
        heroes.append(Cashmere)

        
        loop.loadingScreen()
        os.system("cls")
        
        input("Press Enter to proceed. ")
        
        Ceres.currentHealth = 90
        Ceres.currentEnergy = 45
        Jade.currentHealth = 120
        Jade.currentEnergy = 50
        Kelsey.currentHealth = 75
        Kelsey.currentEnergy = 55
        Cashmere.currentHealth = 140
        Cashmere.currentEnergy = 75

        game = Game(heroes, enemies)
        enemies = []

        enemies.clear()
        voraciousSpider = Enemy("Voracious Spider", 80, 80, 15, {"String Shot", "Venom Shot", "Lunge"}, "A")
        undeadMiner = Enemy("Undead Miner", 110, 110, 7.5, {"Shovel Whack", "Shovel Smack"}, "B")
        bat = Enemy("Bat", 20, 20, 20, {"Nibble", "Blood Ichor"}, "C")
        enemies.append(voraciousSpider)
        enemies.append(undeadMiner)
        enemies.append(bat)
        
        while True:
            game.heroSelect()
            if game.selectedHero:
                combatActive = game.combatTurn()
                if not combatActive:
                    break
            else:
                break
        
        loop.loadingScreen()
        os.system("cls")

        currentLevel = 2
        currentLevelUltimateModifier = 1

        stab = Attack(30, 20, "Stab", isHealing = False)
        powerhit = Attack(25, 20, "Power Hit", isHealing = False)
        whittle = Attack(5, 1, "Whittle", isHealing = False)
        whack = Attack(10, 10, "Whack", isHealing = False)

        Ceres = Hero(playerName, 105, 105, 50, 100, 7.5, currentLevel, [("Basic Attack", "A", basicattack), ("Slice", "B", sliceattack), ("Stab", "C", stab)], "A")
        Jade = Hero("Jade", 130, 130, 60, 120, 5, currentLevel, [("Basic Attack", "A", basicattack), ("Headbutt", "B", headbutt), ("Power Hit", "C", powerhit)], "B")
        Kelsey = Hero("Kelsey", 80, 80, 65, 130, 15, currentLevel, [("Basic Attack", "A", basicattack), ("Slam", "B", slam), ("Whittle", "C", whittle)], "C")
        Cashmere = Hero("Cashmere", 150, 150, 85, 170, 10, currentLevel, [("Basic Attack", "A", basicattack), ("Cook", "B", cook), ("Whack", "C", whack)], "D")
        
        input("Entering Jash's shop. Press Enter to proceed. ")

        player = inShop.Player(playerName, 500)
        strengthItem = inShop.Item("Strength Modifier", 40, 1, "A")
        movesetConsumable00 = inShop.Item("Moveset Consumable 00", 350, 1, "B")

        merchant = inShop.Merchant("Jash")
        merchant.add_item(strengthItem)
        merchant.add_item(movesetConsumable00)

        while True:
            os.system("cls")
            merchant.list_items()
            boughtItem = input("Input the letter corresponding to the item you would like to buy. ").strip().upper()

            items = list(merchant.inventory.values())
            validLetters = [item.position for item in items]

            if boughtItem not in validLetters:
                input("Invalid input. Press enter to try again. ")
                continue

            boughtItemSelected = next(item for item in items if item.position == boughtItem)
            boughtItemName = boughtItemSelected.name

            boughtItemAmt = (input("How many would you like to buy? ")).strip()
            try:
                boughtItemAmt = int(boughtItemAmt)
                if boughtItemAmt <= 0:
                    input("Quantity must be greater than 0. Press Enter to continue. ")
                    continue
            except ValueError:
                input("Invalid quantity. Press Enter to try again. ")
                continue

            os.system('cls')
            merchant.sell_item(player, boughtItemName, boughtItemAmt)

            print(player)
            print(merchant)
            
            while True:
                continueChoice = input("Continue? Y/N ").strip().lower()
                if continueChoice in ["y", "yes"]:
                    if merchant.inventory:
                        os.system("cls")
                        merchant.list_items()
                        break
                    else:
                        os.system("cls")
                        input("Invalid selection. Press Enter to retry. ")
                elif continueChoice in ["n", "no"]:
                    break
                else:
                    input("Invalid input. Press Enter to try again.")
            if continueChoice in ["n", "no"]:
                break               
        
        os.system("cls")
        loop.delayPrint(1.5, "[Jash] Hehe... Pleasure doing business...")
        time.sleep(1.5)
        input("Press Enter to open the inventory. ")
        time.sleep(3)
        os.system("cls")
        print(player)
        while True:
            if not player.inventory:
                input("Nothing in the inventory to use. Press Enter to continue. ")
                break
            useItemsInInventory = input("Would you like to use anything in the inventory? Y/N ").strip().lower()
            if useItemsInInventory not in ["y", "n", "yes", "no"]:
                loop.delayPrint(2.5, "Invalid input. Try again.")
            elif useItemsInInventory in ["y", "yes"]:
                os.system("cls")
                loop.delayPrint(1, player)
                
                print("Items in your inventory:")
                for item in player.inventory.values():
                    print(f"{item} [{item.position}]") 

                itemLetter = input("Which item would you like to use? Input the corresponding letter: ").strip().upper()

                inventoryItems = list(player.inventory.values())
                validLetters = [item.position for item in inventoryItems]

                if itemLetter not in validLetters:
                    loop.delayPrint(2, "Invalid selection. Try again.")
                    continue

                itemToUse = next(item for item in inventoryItems if item.position == itemLetter)

                if itemToUse:
                    print(f"Are you sure you want to use {itemToUse.name}? (Y/N)")
                    useConfirm = input().strip().lower()
                    if useConfirm in ["y", "yes"]:
                        player.use_item(itemToUse.name)
                        loop.delayPrint(1.5, f"{itemToUse.name} has been used.")
                        if itemToUse.name == "Moveset Consumable 00":
                            trick = Attack(40, 65, "Trick", isHealing = False)
                            global usedTrick
                            usedTrick = True
                        elif itemToUse.name == "Strength Modifier":
                            global temporaryLevel
                            temporaryLevel = 3
                            currentLevel = temporaryLevel
                            global temporaryLevelUltimateModifier
                            temporaryLevelUltimateModifier = 1.25
                            currentLevelUltimateModifier = temporaryLevelUltimateModifier
                        continue
                    else:
                        loop.delayPrint(1.5, "Item use canceled.")
                        break
                else:
                    loop.delayPrint(2, "Item not found.")
            elif useItemsInInventory in ["n", "no"]:
                loop.delayPrint(1, "Very well. Closing inventory...")
                break
        loop.loadingScreen()
        os.system("cls")
        input("Press Enter to proceed. ")
        loop.loadingScreen()
        os.system("cls")

        Ceres.currentHealth = 105
        Ceres.currentEnergy = 50
        Jade.currentHealth = 130
        Jade.currentEnergy = 60
        Kelsey.currentHealth = 80
        Kelsey.currentEnergy = 65
        Cashmere.currentHealth = 150
        Cashmere.currentEnergy = 85

        enemies.clear()
        bat = Enemy("Bat", 20, 20, 20, {"Nibble", "Blood Ichor"}, "A")
        voraciousSpider = Enemy("Voracious Spider", 80, 80, 15, {"String Shot", "Venom Shot", "Lunge"}, "B")
        arachne = Enemy("Arachne", 300, 300, 25, {"Noxious Shot", "Blood Harvest", "Bite"}, "C")
        voraciousSpider2 = Enemy("Voracious Spider", 80, 80, 15, {"String Shot", "Venom Shot", "Lunge"}, "D")
        bat2 = Enemy("Bat", 20, 20, 20, {"Nibble", "Blood Ichor"}, "E")
        enemies.append(bat)
        enemies.append(voraciousSpider)
        enemies.append(arachne)
        enemies.append(voraciousSpider2)
        enemies.append(bat2)

        if usedTrick:
            Ceres.moveset.append(("Trick", "00", trick))

        while True:
            game.heroSelect()
            if game.selectedHero:
                combatActive = game.combatTurn()
                if not combatActive:
                    break
            else:
                break

        loop.loadingScreen()
        os.system("cls")

        loop.delayPrint(1, "test")

    def delayPrint(delaySeconds, printString):
        time.sleep(delaySeconds)
        print(printString)

loop.mainLoop()