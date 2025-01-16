import os
import random
import time
import inShop

global usedTrick
usedTrick = False
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
        return f"{self.name}"

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
        totalDmg = 1.5 * self.strength
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
                        healingPercentage = 37.5
                        print(f"{move} [{letter}] (Cost: {attack.energyCost} Energy, Heals: {healingPercentage}% HP)")
                    elif attack.name == "Group Heal":
                        healingPercentage = 20
                        print(f"{move} [{letter}] (Cost: {attack.energyCost} Energy, Heals: {healingPercentage}% of each ally's max HP, and heals slightly less for Cashmere)")
                    elif attack.name == "Energy Support":
                        supportPercentage = 10
                        print(f"{move} [{letter}] (Cost: {attack.energyCost} Energy, Regenerates {supportPercentage}% of one ally's max energy.)")
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
                                if attack.name == "Group Heal" or attack.name == "Cook" or attack.name == "Energy Support":
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
                        healAmount = ally.maxHealth * 0.375
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
            elif attack.name == "Energy Support":
                os.system("cls")
                for ally in availableAllies:
                    print(f"{ally.name} [{ally.position}] - Energy: {ally.currentEnergy} / {ally.maxEnergy}")

                allyPosition = input("Enter the position of the ally to support: ").strip().upper()

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
                        supportAmount = ally.maxEnergy * 0.15
                        ally.currentEnergy += supportAmount
                        if ally.currentEnergy > ally.maxEnergy:  
                            ally.currentEnergy = ally.maxEnergy
                        os.system("cls")
                        print(f"{self.selectedHero.name} regenerates {ally.name} {supportAmount:.2f} Energy! ({ally.currentEnergy} / {ally.maxEnergy})")
                        input("Press Enter to continue.")
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
            displayedTip = "Tip: There is a secret code that activates easy mode! Don't try to find it, though. You won't find it."
        elif randomTip == 11:
            displayedTip = "Tip: This project is brought to you by a poorly designed garble of spaghetti code. Please do not test its limits or it will cry. And then I will cry. "
        print(displayedTip)
    def loadingScreen():
        os.system("cls")
        print("Loading . . . ")
        loop.tips()
        time.sleep(1)
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
        """
        loop.delayPrint(2.5, "Your eyes creep open as you slowly pick yourself up from the ground.") # new
        loop.delayPrint(3, "Brilliant white pillars of marble rise from the ground, stretching into the sky above.") # new
        loop.delayPrint(3, "In front of you, a being of massive proportions sits upon a throne of marble. He raises his voice to speak.") # new
        loop.delayPrint(4, "[???] Hello there.")
        loop.delayPrint(2, "[???] What are you doing here?")
        loop.delayPrint(2, "[You] ...what?") # "[Nameless] What...?"
        loop.delayPrint(2, "[???] Why are you here? Who are you?") # "[???] Who are you? Why are you here?
        time.sleep(2)
        print("[You] I don't know. Who am I?") # [Nameless] Good question... Who am I?"""
        time.sleep(2)
        global playerName
        yes = True
        while yes:
            playerName = input("Who are you? ").strip()
            if not playerName:
                input("[???] Speak up. (Press Enter to retry.) ")
                os.system("cls")
            elif playerName == "Queenie":
                time.sleep(1)
                yes = False
                confirm = input(f"The name 'Queenie' absolutely sucks. Are you absolutely sure you want to go through with this? (Y/N) ")
                if confirm not in ["y", "yes", "n", "no"]:
                    input("Invalid input. Try again. ")
                elif confirm in ["y", "yes"]:
                    print("Alright, your loss.")
                    time.sleep(2)
                    break
                elif confirm in ["n", "no"]: # optimize the checking system. .upper() or something and remove the lists
                    yes = True
            else:
                loop.delayPrint(1, f"My name is {playerName}.")
                yes = False
                confirm = input(f"Your name is {playerName}? Y/N ")
                if confirm not in ["y", "yes", "n", "no"]:
                    input("Invalid input. Try again. ")
                elif confirm in ["y", "yes"]:
                    break
                elif confirm in ["n", "no"]:
                    yes = True
        os.system("cls")
        """
        loop.delayPrint(3, "[???] Ah.") # "[???] Hm."
        loop.delayPrint(2, f"[???] '{playerName}'.") # "[???] {playerName}?"
        loop.delayPrint(2, "[???] Your name is the worst name I have ever heard.")
        loop.delayPrint(2, "[???] You seem lost. ") # "[???] Whatever... You seem lost. "
        loop.delayPrint(1.4, "[???] Confused, perhaps.") # "[???] Confused, perhaps...?"
        loop.delayPrint(2.5, f"[{playerName}] Yeah... Where am I?") # new
        loop.delayPrint(2, f"[???] You are currently in my temple. Isn't it so beautiful?") # "[???] Let me explain: Your name is {playerName}, apparently, and you are in my temple."
        loop.delayPrint(3.5, "'No,' you think to yourself.") # new
        loop.delayPrint(2, "[???] Well, I must ask you to leave now. I have more important matters to focus on right now.") # "[???] I'm pretty busy right now, so I'm going to kindly ask you to leave."
        loop.delayPrint(3.5, "No, I won't leave until you give me answers.") # "..."
        loop.delayPrint(2, "Who are you, where am I, and how did I get here?") # new
        loop.delayPrint(2, "The figure sighs.") # new
        loop.delayPrint(2.5, "My identity is of no concern to you. Also, I already answered the second question. You're in my tem-") # new
        loop.delayPrint(4, "' - Who are you???' you interject. He stops speaking.") # new
        loop.delayPrint(3, "[???] You dare cut off a God while he speaks?") # new
        loop.delayPrint(3, f"[{playerName}] ... I really... don't care... I just want answers...") # new
        loop.delayPrint(2.5, "The figure sighs before standing up from his throne. A staff materializes in his hand, and he points it at you.") # new
        loop.delayPrint(5.5, f"[???] Prepare yourself. Your name will be erased from the annals of history.") # new"""
        time.sleep(2)
        # moves
        basicattack = Attack(damage = 5, energyCost = -17.5, name = "Basic Attack", isHealing = False)
        sliceattack = Attack(damage = 10, energyCost = 10, name = "Slice", isHealing = False)

        # characters/heroes
        global currentLevel
        Ceres = Hero(playerName, 90, 90, 45, 90, 5, currentLevel, [("Basic Attack", "A", basicattack), ("Slice", "B", sliceattack)], "A")
        heroes = [Ceres]

        # enemies
        Zol = Enemy("???", 100000000, 100000000, 100000000, {"Demolish"}, "A")
        enemies = [Zol]

        game = Game(heroes, enemies)
        while True:
            game.heroSelect()

            if game.selectedHero:
                combatActive = game.combatTurn()
                if not combatActive:
                    break
            else:
                break
        
        os.system("cls")
        """
        loop.delayPrint(4, "[???] You have been defeated.")
        loop.delayPrint(1.5, "[???] 'Now leave'") # new
        loop.delayPrint(2, "Your vision starts to fade to black... ")
        time.sleep(2.5)
        loop.loadingScreen()
        os.system("cls")
        loop.delayPrint(3, "[???] Hello?")
        loop.delayPrint(3, "Your eyes slowly open once more. This time, you lay on a soft bed of grass.") # new
        loop.delayPrint(2.5, "[???] Oh my, are you okay??")
        loop.delayPrint(2, "[???] You seem to be covered in bruises...") # "[???] Damn, you seem really bruised..."
        loop.delayPrint(2.5, "[???] Stand up! Follow me, I will find you aid!") # "[???] Follow me, I'll get you some help!"
        time.sleep(3)
        os.system("cls")
        loop.delayPrint(3, "The unknown person carries you over her shoulder to a nearby campsite..." ) # The unknown person drags you to a campsite . . .
        time.sleep(3)
        os.system("cls")
        loop.delayPrint(5, "[???] What happened to you? Your bruises look like they cover your whole body...") # "[???] What happened to you? You are in really bad shape..."
        loop.delayPrint(2, "[???] Just wait a little longer, one of my friends will be able to help you recover from your wounds.") # "[???] Don't worry, I know a guy who can help for things like this." 
        loop.delayPrint(3, "'Thank you,' you tell her. She gives you a smile before you two sit in awkward silence.") # new
        loop.delayPrint(5, "[???] ...my name is Jade. And what might your name be?") # "[???] Oh! By the way, I'm Jade. Who might you be? "
        loop.delayPrint(3, f"I'm {playerName}.")
        loop.delayPrint(2.5, "[Jade] I see. A strange name, but you do not seem to be from around here anyways.") # "[Jade] I see. Strange name, but then again, you don't look like an normal, average guy."
        loop.delayPrint(2.5, "[Jade] The others should be arriving soon.")
        loop.delayPrint(3.5, "[Jade] The forest surrounding us is filled with dangerous monsters, so they might be caught up with fighting them.")
        loop.delayPrint(5, "The awkward silence returns.") 
        loop.delayPrint(2.5, "[Jade] Now that I think about it, it has been a while since they have went out. I might have to look for them...")
        loop.delayPrint(4, "[Jade] Do not worry, though. You will be in good hands soon.")
        loop.delayPrint(2, "[Jade] Follow me. I will go look for them.")
        loop.delayPrint(4.5, "Jade leads the way as she tries searching for her party.")
        loop.delayPrint(5, "Just then, you hear the rustling of leaves in the distance.")
        loop.delayPrint(3.5, "[Jade] That sounds like commotion. I wonder what is happening?")
        loop.delayPrint(2.5, "The two of you venture closer to the source of the noise...")
        time.sleep(5)
        loop.loadingScreen()
        os.system("cls")
        loop.delayPrint(3.5, "You see two individuals in the distance fighting against a particularly large foe...")
        loop.delayPrint(2, "[Jade] I think those are my friends. Quickly, we must help them!")
        time.sleep(3)"""
        loop.loadingScreen()
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

        enemies.clear()
        yeOldeGnome = Enemy("Ye Olde Gnome", 200, 200, 15, {"Shrubbage", "Roll Over", "Stomp"}, "A")
        enemies.append(yeOldeGnome)
        
        while True:
            if Ceres.currentHealth <= 0 and Jade.currentHealth <= 0 and Kelsey.currentHealth <= 0 and Cashmere.currentHealth <= 0:
                raise SystemExit
            game.heroSelect()
            if game.selectedHero:
                combatActive = game.combatTurn()
                if not combatActive:
                    break
            else:
                break
        loop.loadingScreen()
        os.system("cls")
        """
        loop.delayPrint(3.5, "[?] Damn, that guy was way tougher than usual...")
        loop.delayPrint(2.5, "[??] Exactly! I didn't even know there were monsters as big as him here.")
        loop.delayPrint(3.75, "[Jade] I am glad you guys are all okay.")
        loop.delayPrint(2.5, f"[Jade] {playerName}, this is Kelsey and Cashmere. Kelsey and Cashmere, this is {playerName}.")
        loop.delayPrint(3, "[Jade] I found him near our campsite looking horribly disheveled, and I wanted to see if you two could do anything about it.")
        loop.delayPrint(2.5, "[Cashmere] Duh, obviously we can do something about it.")
        loop.delayPrint(6.5, "Back at the campsite, Kelsey tends to your wounds while Cashmere cooks something over a fire.")
        loop.delayPrint(2, "[Kelsey] That's only a temporary fix, though. We should probably find a shop, or hospital, or something to help you feel better.")
        loop.delayPrint(1.5, f"[Jade] Yeah, we also have to decide what to do with {playerName} once he's fixed up. ")
        loop.delayPrint(2, f"[Kelsey] Oh, yeahhh! Where did you even come from, {playerName}?")
        loop.delayPrint(2.5, "'A good question,' you think to yourself. You try to recall memories of your past, but all you see are the marble pillars reaching above.")
        loop.delayPrint(3.5, f"You tell them what you remembered, but they stare at you with blank faces.")
        loop.delayPrint(4, "[Kelsey] ...I think he's still in shock.")
        loop.delayPrint(2.5, "[Jade] I agree, that is quite the strange backstory.")
        loop.delayPrint(2.5, f"[Kelsey] When I was tending to {playerName}'s wounds, I noticed a strange mark on their forearm. Do any of you know what that is?")
        loop.delayPrint(3, "The other party members crowd around you, staring at the mark. ")
        loop.delayPrint(2, "[Jade] Yikes.... We should not touch that. What if it's dangerous?")
        loop.delayPrint(3.5, f"[Cashmere] Good point. Let's go. We'll figure out what to do with {playerName} eventually.")
        loop.delayPrint(4.5, "Now with a newfound group, you head to a campsite on the edge of the forest.")
        time.sleep(1.5)
        input("Press Enter to continue.")
        loop.loadingScreen()
        os.system("cls")
        loop.delayPrint(4, "[Kelsey] I can't WAIT for you to see our campsite! It's got so much cool stuff, and there's so much nature stuff, and like there's-")
        loop.delayPrint(1.5, "[Jade] Oh, be quiet Kel. You are ruining the surprise.")
        loop.delayPrint(2.5, f"[Kelsey] What? I'm just excited to show {playerName} our accomplishment, is that unreasonable?")
        loop.delayPrint(2, f"[Jade] I am not saying that it is unreasonable, I am just saying that maybe {playerName} might want to find out for themself...")
        loop.delayPrint(2.5, "[Kelsey] Well SORRY for slightly disrupting the plan that YOU never told us...")
        loop.delayPrint(1.5, "[Jade] Are you serious?")
        loop.delayPrint(4.5, "[Cashmere] Yo, you might want to check this out...")
        loop.delayPrint(1.5, "[Kelsey] WHAT DO YOU MEAN, 'are you serious'?????")
        loop.delayPrint(2, "[Jade] WHAT I MEAN IS THAT MAYBE YOU SHOULD NOT BE SO LOUD-MOUTHED????")
        loop.delayPrint(2.5, "[Cashmere] Yo, look at the damn camp-")
        loop.delayPrint(2.5, "You watch in silence as Jade and Kelsey bicker at each other.")
        loop.delayPrint(2.25, "[Kelsey] THERE IS NO WAY WE'RE GETTING INTO THIS RIGHT NOW IN FRONT OF THE NEW GUY!")
        loop.delayPrint(2, "[Jade] THIS WOULD HAVE NEVER HAPPENED IF YOU COULD CONTROL YOURSELF FOR JUST ONE MOMENT!")
        loop.delayPrint(1, "[Cashmere] THE CAMPSITE IS GONE YOU IDIOTS")
        time.sleep(5)
        print("[Jade] WHAT")
        loop.delayPrint(0.2, "[Kelsey] WHAT")
        loop.delayPrint(0.5, "What?")
        loop.delayPrint(2, "Cashmere is right. The group's so-called 'campsite' now seems to be nothing but a bunch of crumpled up tents and clothes.")
        loop.delayPrint(1, "The fire in the center has been extinguished. There are also some seemingly foreign markings etched into the ground. ")
        loop.delayPrint(2, "[Jade] Oh my lord. Dear lord.")
        loop.delayPrint(2, "[Kelsey] Where is Clove?")
        loop.delayPrint(1.5, "Clove? You figure he must be another one of their troupe.")
        loop.delayPrint(2, "[Cashmere] Ugh, you're right. He's gone missing.")
        loop.delayPrint(3, "[Cashmere] I can't find any sign of him anywhere. Maybe he just wandered off?")
        loop.delayPrint(1, "[Jade] Look! His tent is destroyed. Someone must have taken him away.")
        loop.delayPrint(1.5, "Kelsey buries his face in his hands.")
        loop.delayPrint(3, "[Kelsey] Well isn't this just the best day ever.")
        loop.delayPrint(2.5, "[Cashmere] Calm down guys. We're gonna find him.")
        loop.delayPrint(1, "[Kelsey] You don't even know that for sure, shut up.")
        loop.delayPrint(1.5, "[Cashmere] What, are we just going to give up on searching for him?")
        loop.delayPrint(1, "[Jade] He is right.")
        loop.delayPrint(2.5, "[Kelsey] Jade, shut up already.")
        loop.delayPrint(1.5, "[Cashmere] Calm down, everyone. Do you all remember the caves we discovered a while back near here?")
        loop.delayPrint(2, "[Cashmere] We could try exploring there.")
        loop.delayPrint(2.5, "[Kelsey] Alright, but it's gonna be dangerous.")
        loop.delayPrint(1, "[Cashmere] Clove could also be in danger.")
        loop.delayPrint(1.5, "[Jade] Come on, we should go already...")
        loop.delayPrint(2, "The three go on and walk towards the cave, completely disregarding your opinion. You decide to follow them.")
        loop.loadingScreen()
        os.system("cls")
        loop.delayPrint(1.5, "The group has dragged you along with them for the second or third time today, and this time, you're going along with them to what's supposed to be a super dangerous cave. ")
        loop.delayPrint(1, "[Cashmere] This should be it up ahead.")
        loop.delayPrint(1.5, "[Jade] Yikes... This place is still so creepy...")
        loop.delayPrint(1, "[Kelsey] I guess we just head in?")
        loop.delayPrint(2, "[Cashmere] Not so fast there. We need to make sure everything is ready and that we're all healthy.")
        loop.delayPrint(1.5, "[Cashmere] It wouldn't be wise to just head in face-first, as we could really suffer consequences.")
        loop.delayPrint(2.5, "[Cashmere] There are a bunch of monsters lurking in here, and it would be really easy to get surrounded if we don't plan this strategically.")
        loop.delayPrint(1, "[Cashmere] I propose we draft a plan of attack before we go in. Kelsey?")
        loop.delayPrint(2, "[Cashmere] Kelsey?")
        loop.delayPrint(0.5, "[Jade] Kelsey's already ran in a while ago.")
        loop.delayPrint(1, "[Cashmere] God damn it.")
        loop.delayPrint(2, "[Cashmere] I guess we just follow him in then...")
        loop.loadingScreen()
        os.system("cls")
        loop.delayPrint(1, "[Cashmere] KELSEY! ARE YOU THERE?")
        loop.delayPrint(2.5, "[Jade] KEL??")
        loop.delayPrint(5.5, "[Kelsey] CHECK OUT THIS SHINY ROCK!!")
        loop.delayPrint(3.5, "Out of what seems to be nowhere, Kelsey runs towards the three of you, holding a particularly lustrous rock.")
        loop.delayPrint(1, "[Kelsey] Isn't this so cool??")
        loop.delayPrint(2.5, "[Cashmere] ... Kelsey, you shouldn't be picking up random things in the wilderness...")
        loop.delayPrint(1, "[Kelsey] But it's... so shiny...")
        loop.delayPrint(1.5, "[Kelsey] And when you rub it... it makes such a cool sound!! Look!")
        loop.delayPrint(1, "Before anyone can object, Kelsey starts rubbing the rock in his hand, and it starts resonating...")
        loop.delayPrint(3.5, "[Jade] You're really stupid, you know that?")
        loop.delayPrint(1.5, "[Kelsey] What, so I can't have cool things anymore??")
        loop.delayPrint(2, "[Cashmere] Not if we don't know what those cool things are... or what they could do... ")
        loop.delayPrint(1.5, "[Kelsey] YEAH RIGHT... Like anything bad could ever happen from such a cool rock...")
        loop.delayPrint(3, "Kelsey throws the rock at a cavern wall, and suddenly, monsters materialize out of thin air...")
        loop.delayPrint(2.5, "[Jade] What do you define as 'anything bad', exactly?")
        loop.delayPrint(1.5, "[Cashmere] Now's not the time to bicker, guys. Get ready to fight...")"""
        input("Press Enter to proceed. ")
        
        Ceres.currentHealth = 90
        Ceres.currentEnergy = 45
        Jade.currentHealth = 120
        Jade.currentEnergy = 50
        Kelsey.currentHealth = 75
        Kelsey.currentEnergy = 55
        Cashmere.currentHealth = 140
        Cashmere.currentEnergy = 75

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
        global currentLevelUltimateModifier
        currentLevelUltimateModifier = 1

        stab = Attack(30, 20, "Stab", isHealing = False)
        powerhit = Attack(25, 20, "Power Hit", isHealing = False)
        whittle = Attack(5, 1, "Whittle", isHealing = False)
        whack = Attack(10, 10, "Whack", isHealing = False)

        Ceres.currentHealth = 105
        Ceres.maxHealth = 105
        Ceres.currentEnergy = 50
        Ceres.maxEnergy = 100
        Ceres.energyRegen = 7.5
        Ceres.moveset.append(("Stab", "C", stab))
        Jade.currentHealth = 130
        Jade.maxHealth = 130
        Jade.currentEnergy = 60
        Jade.maxEnergy = 120
        Jade.energyRegen = 5
        Jade.moveset.append(("Power Hit", "C", powerhit))
        Kelsey.currentHealth = 80
        Kelsey.maxHealth = 80
        Kelsey.currentEnergy = 65
        Kelsey.maxEnergy = 130
        Kelsey.energyRegen = 15
        Kelsey.moveset.append(("Whittle", "C", whittle))
        Cashmere.currentHealth = 150
        Cashmere.maxHealth = 150
        Cashmere.currentEnergy = 85
        Cashmere.maxEnergy = 170
        Cashmere.energyRegen = 10
        Cashmere.moveset.append(("Whack", "C", whack))
        """
        loop.delayPrint(1.5, "[Jade] Kel, I really hope you're done being an idiot.")
        loop.delayPrint(1.5, "[Kelsey] Sorry, I didn't know...")
        loop.delayPrint(2, "[Cashmere] Kelsey, you really should know better than this...")
        loop.delayPrint(0.5, "[Kelsey] I didn't know!! How is any of this my fault?")
        loop.delayPrint(1.5, "[Cashmere] Err...")
        loop.delayPrint(2.5, "[Jade] Considering how the rock YOU threw summoned those monsters, I'd say the entirety of this is your fault...")
        loop.delayPrint(1, "[Kelsey] Whatever, let's keep going forward. ")
        loop.delayPrint(1.5, "[Kelsey] Maybe we'll find something.")
        loop.delayPrint(2, "[Jade] Uhguidhgjfdghdfhgkjg...")
        loop.loadingScreen()
        os.system("cls")
        loop.delayPrint(1.5, "The crew ventures further into the cave, and a while later, Kelsey stumbles upon an opening in one of the walls. ")
        loop.delayPrint(2, "[Kelsey] Yo guys! Check this out!!")
        loop.delayPrint(2.5, "[Jade] What now...?")
        loop.delayPrint(2, "[Kelsey] I swear it's not anything bad this time! Look! There's a little hole here!")
        loop.delayPrint(3.5, "You lean in to investigate... Suddenly, a strange little figure pokes its head out of the hole...")
        loop.delayPrint(2.5, "[???] Hello, young travelers.")
        loop.delayPrint(3, "[Jade] EW EW EW WHAT IS THAT GET IT AWAY FROM ME IT'S SO UGLY")
        loop.delayPrint(1.5, "[Cashmere] Calm down. It seems to be a... person?")
        loop.delayPrint(1.5, "[???] Fear not, young adventurers. I am not here to hurt, but to help. You may call me JASH.")
        loop.delayPrint(2, "[Jade] Jash is a horrible name...")
        loop.delayPrint(1, "[Jash] I'm aware.")
        loop.delayPrint(1.5, "[Jash] Anyhow, I would like to lend my assistance... for a price.")
        loop.delayPrint(3, "A price...?")
        loop.delayPrint(2, "[Jash] This price... it is a mythical currency. It may be quite common, but do not let its rarity fool you. This commodity is quite valuable, when handled by the right person...")
        loop.delayPrint(1.5, "[Cashmere] Is it... money...?")
        loop.delayPrint(1, "[Jash] That is correct.")
        loop.delayPrint(1.5, "[Jade] Could've just said that...")
        loop.delayPrint(2, "[Jash] I am not here to debate about specific details. Would you like to purchase items from me?")"""
        
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
        loop.delayPrint(1, "And within a fraction of a second, Jash disappears...")
        loop.delayPrint(2, "[Jade] What a strange little guy...")
        loop.delayPrint(1.5, "[Kelsey] Weren't you literally screaming at it to go away just now?")
        loop.delayPrint(3, "[Jade] I'm a changed woman.")
        loop.delayPrint(2.5, "[Kelsey] You're a hypocrite, is what you are...")
        loop.delayPrint(2.5, "[Cashmere] Calm down, you two... We're going to have to not fight if we want to be able to find Clove and be able to make it out of here...")
        loop.delayPrint(1.5, "[Jade] Don't me telling me to calm down, Kel's the one who started it...")
        loop.delayPrint(2, "[Cashmere] Whatever, let's just stick together and keep going.")
        loop.delayPrint(3, "[Cashmere] I really hope we're able to find Clove soon...")
        loop.delayPrint(2, "[Jade] Ugh... ")
        loop.loadingScreen()
        os.system("cls")
        loop.delayPrint(2, "You venture even deeper into the cave, not sure if you're lost... Hopefully someone else is keeping track of where you're going.")
        loop.delayPrint(2.5, "As you make another turn, you seem to be getting some vague sense of deja vu...")
        loop.delayPrint(2, "[Kelsey] Hey, is it just me or like are we going in the same direction?")
        loop.delayPrint(2.5, "[Cashmere] What do you mean?")
        loop.delayPrint(3, "[Kelsey] Like... have we not been in this exact spot like 5 minutes ago??")
        loop.delayPrint(2, "[Jade] Maybe we're losing ourselves. Let's go back before it's too late.")
        loop.delayPrint(1.5, "Alright, then... It seems like you're just going to have to tag along with whatever the group decides to do.")
        loop.delayPrint(2, "The four of you search for an exit... ")
        loop.loadingScreen()
        os.system("cls")
        loop.delayPrint(3, "[Kelsey] Guys?? I don't think I'm finding any exits...")
        loop.delayPrint(2.5, "[Jade] Me neither... I think we're lost...")
        loop.delayPrint(1.5, "[Cashmere] Shoot. We need to find an exit before any monsters get to us... We don't know what these guys are capable of.")
        loop.delayPrint(2.5, "[Jade] Oh yeah my bad let me just find an exit real quick even though I literally JUST SAID I COULDN'T")
        loop.delayPrint(3, "[Cashmere] Let's please not get into this right now...")
        loop.delayPrint(2.5, "[Kelsey] What are we supposed to do here?")
        loop.delayPrint(3, "[Cashmere] Let's look around. Maybe we'll find someone or something who can help.")
        loop.loadingScreen()
        os.system("cls")
        loop.delayPrint(5, "Still no progress... Your legs really want to take a break...")
        loop.delayPrint(2.5, "[Kelsey] I really dont think we're gonna be able to get out of here...")
        loop.delayPrint(3, "[Jade] Hold on... Look there!")
        loop.delayPrint(2.5, "All of your heads turn towards where Jade is pointing towards.")
        loop.delayPrint(2, "There doesn't seem to be anything there...")
        loop.delayPrint(3, "[Kelsey] Oh yeah, air. That's definitely gonna help, Jade.")
        loop.delayPrint(2.5, "[Jade] No, no, no, look closer!")
        loop.delayPrint(3, "[Cashmere] Shut up, Kelsey. I think I see something...")
        loop.delayPrint(2.5, "[Jade] I think it's... some sort of light??")
        loop.delayPrint(3, "[Kelsey] Oh my god this is it... We're going to heaven...")
        loop.delayPrint(2.5, "[Jade] ??? Shut up, Kel.")
        loop.delayPrint(3, "[Cashmere] Let's investigate, guys.")
        loop.delayPrint(3.5, "The four of you inch closer towards the mysterious light, but before you can make any progress...")
        loop.delayPrint(1.5, "A monster jumps from the walls and ambushes the group!")
        loop.delayPrint(2, "[Cashmere] Shoot. Get ready, everyone!")
        input("Press Enter to proceed. ")
        loop.loadingScreen()
        os.system("cls")

        enemies.clear()
        
        del(bat)
        bat = Enemy("Bat", 20, 20, 15, {"Nibble", "Blood Ichor"}, "A")
        del(voraciousSpider)
        voraciousSpider = Enemy("Voracious Spider", 80, 80, 5, {"String Shot", "Venom Shot", "Lunge"}, "B")
        arachne = Enemy("Arachne", 300, 300, 15, {"Noxious Shot", "Blood Harvest", "Bite"}, "C")
        voraciousSpider2 = Enemy("Voracious Spider", 80, 80, 5, {"String Shot", "Venom Shot", "Lunge"}, "D")
        bat2 = Enemy("Bat", 20, 20, 15, {"Nibble", "Blood Ichor"}, "E")
        
        enemies.append(bat)
        enemies.append(voraciousSpider)
        enemies.append(arachne)
        enemies.append(voraciousSpider2)
        enemies.append(bat2)
        if usedTrick:
            Ceres.moveset.append(("Trick", "00", trick))

        while True:
            if Ceres.currentHealth <= 0 and Jade.currentHealth <= 0 and Kelsey.currentHealth <= 0 and Cashmere.currentHealth <= 0:
                raise SystemExit
            game.heroSelect()
            if game.selectedHero:
                
                combatActive = game.combatTurn()
                if not combatActive:
                    break
            else:
                break
            
            
        loop.loadingScreen()
        os.system("cls")

        currentLevel = 3
        currentLevelUltimateModifier = 1.25

        curveball = Attack(random.randint(Kelsey.level * 2, Kelsey.level * 2 + 35), random.randint(round(Kelsey.maxEnergy / 10), round(Kelsey.maxEnergy / 6)), "Curveball", isHealing = False)
        groupHeal = Attack(20, 25, "Group Heal", isHealing = True)
        strike = Attack(40, 25, "Strike", isHealing = False)
        energySupport = Attack(0, 15, "Energy Support", isHealing = True)

        Ceres.moveset.append(("Strike", "D", strike))
        Jade.moveset.append(("Energy Support", "D", energySupport))
        Kelsey.moveset.append(("Curveball", "D", curveball))
        Cashmere.moveset.append(("Group Heal", "D", groupHeal))

        Ceres.currentHealth = 125
        Ceres.maxHealth = 125
        Ceres.currentEnergy = 65
        Ceres.maxEnergy = 130
        Ceres.energyRegen = 15
        Jade.currentHealth = 155
        Jade.maxHealth = 155
        Jade.currentEnergy = 75
        Jade.maxEnergy = 150
        Jade.energyRegen = 7.5
        Kelsey.currentHealth = 90
        Kelsey.maxHealth = 90
        Kelsey.currentEnergy = 75
        Kelsey.maxEnergy = 150
        Kelsey.energyRegen = 17.5
        Cashmere.currentHealth = 170
        Cashmere.maxHealth = 170
        Cashmere.currentEnergy = 95
        Cashmere.maxEnergy = 190
        Cashmere.energyRegen = 15
        for hero in heroes:
            hero.level = currentLevel

        enemies.clear()
        arachne2 = Enemy("Arachne, Reborn", 450, 450, 30, {"Noxious Shot", "Blood Harvest", "Bite", "Blood Ichor"}, "A")
        enemies.append(arachne2)

        loop.delayPrint(2, "[Jade] What... was that...?")
        loop.delayPrint(3, "[Kelsey] No clue, all I know is that we gotta get out of here, and fast!")
        loop.delayPrint(2.5, "[Cashmere] Yeah. Let's try to find some way out.")
        loop.delayPrint(2, "[Cashmere] We need to stick together, though. We might get ambushed again.")
        loop.delayPrint(2, "Actually not a bad idea! Although, it might be good to check your surroundings.")
        loop.delayPrint(3, "As you turn around, you hear a strange crawling noise that raises all the hairs on your body.")
        loop.delayPrint(2.5, f"[Kelsey] What's the matter, {playerName}?")
        loop.delayPrint(2, "As you point to whatever is behind you, Jade lets out a shriek.")
        loop.delayPrint(2.5, "[Jade] OH MY GOD IT'S ALIVE IT'S ALIVE UGO;IAHSGLKHSAL;DG GET IT AWAY")
        loop.delayPrint(3, "[Cashmere] Shoot. I thought we got rid of it?")
        loop.delayPrint(2.5, "[Cashmere] Whatever. No time to delay. Let's focus on whatever this is first.")
        input("Press Enter to continue. ")

        loop.loadingScreen()
        os.system("cls")

        while True:
            if Ceres.currentHealth <= 0 and Jade.currentHealth <= 0 and Kelsey.currentHealth <= 0 and Cashmere.currentHealth <= 0:
                raise SystemExit
            game.heroSelect()
            if game.selectedHero:
                combatActive = game.combatTurn()
                if not combatActive:
                    break
            else:
                break
        
        player.gold += 350
        loop.loadingScreen()
        os.system("cls")
        
        currentLevel = 4
        currentLevelUltimateModifier = 1.5

        Ceres.currentHealth = 135
        Ceres.maxHealth = 135
        Ceres.currentEnergy = 75
        Ceres.maxEnergy = 150
        Ceres.energyRegen = 17.5
        Jade.currentHealth = 170
        Jade.maxHealth = 170
        Jade.currentEnergy = 80
        Jade.maxEnergy = 160
        Jade.energyRegen = 8
        Kelsey.currentHealth = 95
        Kelsey.maxHealth = 95
        Kelsey.currentEnergy = 80
        Kelsey.maxEnergy = 160
        Kelsey.energyRegen = 18
        Cashmere.currentHealth = 195
        Cashmere.maxHealth = 195
        Cashmere.currentEnergy = 100
        Cashmere.maxEnergy = 200
        Cashmere.energyRegen = 17.5

        loop.delayPrint(1, "test")

    def delayPrint(delaySeconds, printString):
        time.sleep(delaySeconds)
        print(printString)

loop.mainLoop()

# when name confirmation is asked, choosing invalid input just lets the name you typed in be the name.
# choosing no also leads to the "invalid position selected" message to show up again
# hero position is redundant

# seperate functions for dialogue, attacks, and encounters
# use a counter to determine what encounter ur on
# ultimates should be displayed w/ their effect, but your energy has to be enough to actually use it
# all enemy attacks should be displayed in one command without having to press enter multiple time
# round attack damages to the nearest integer
# energy is only added after stats r displayed
# the last dialogue quickly flashes before it goes to a retarded loading screen
# if jash has no more items, it should say in his list "None!"
# if invalid input is given in jash's shop, it should os.cls
# continuing in jash's shop after buying out everything doesnt display the stats. it also says that its invalid input.
# when opening your inventory, it asks for input twice AND says its invalid before asking for the third time.
# when using the moveset consumable, it appends new attacks to EVERYONE's moveset
# whittle (kelsey) is absolutely useless WELL OKAY YOU TRY BEING THAT ATTACK THEN
# after a basic attack is used, it should display your energy regen