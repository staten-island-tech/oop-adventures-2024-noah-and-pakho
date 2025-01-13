import os
import random
import time
import inShop

currentLevel = 1
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
        elif selectedEnemyMove == "String Shot":
            self.stringShotAttack(heroes)
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
        totalDmg = 30
        for hero in heroes:
            if hero.currentHealth > 0:
                hero.currentHealth -= totalDmg
                if hero.currentHealth < 0:
                    hero.currentHealth = 0
                print(f"{self.name} dealt {totalDmg} damage to {hero.name}! ({hero.name} now has {hero.currentHealth} health!)")
        input("Press Enter to continue. ")
    def stringShotAttack(self, heroes):
        print(f"{self.name} uses String Shot! ")
        totalDmg = 15
        for hero in heroes:
            if hero.currentHealth > 0:
                hero.currentHealth -= totalDmg
                if hero.currentHealth < 0:
                    hero.currentHealth = 0
                print(f"{self.name} dealt {totalDmg} damage to {hero.name}! ({hero.name} now has {hero.currentHealth} health!)")

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
                input("Press Enter to exit.")
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

randomTip = random.randint(1, 6)
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
        elif randomTip == 6:
            displayedTip = "Tip: There is a secret code that activates easy mode!"
        print(displayedTip)
    def loadingScreen():
        os.system("cls")
        print("Loading . . . ")
        loop.tips()
        time.sleep(2)
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
            else:
                break
        
        """
        loop.loadingScreen()
        os.system("cls")
        loop.delayPrint(1.5, "[???] Hello there.")
        loop.delayPrint(2, "[???] What are you doing here?")
        loop.delayPrint(3, "What...?")
        loop.delayPrint(2, "[???] Who are you? What are you doing here?")
        loop.delayPrint(3, "[???] Are you there?")
        time.sleep(2)
        print("Good question... Who am I?")
        time.sleep(5)"""
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
        """
        loop.delayPrint(3.5, "[???] Hm.")
        loop.delayPrint(2, f"[???] {playerName}?")
        loop.delayPrint(2, "[???] That's a horrible name.")
        loop.delayPrint(1, "[???] Whatever... You seem lost. ")
        loop.delayPrint(1.5, "[???] Confused, perhaps...?")
        loop.delayPrint(2, f"[???] Let me explain: Your name is {playerName}, apparently, and you are in my temple.")
        loop.delayPrint(4, "[???] I would be way more aggressive, but I'll give you the benefit of the doubt.")
        loop.delayPrint(2.5, "[???] I'm pretty busy right now, so I'm going to kindly ask you to leave.")
        loop.delayPrint(4, "...")
        loop.delayPrint(1.5, "Huh?")
        loop.delayPrint(4, "[???] What do you mean, 'huh' ??")
        loop.delayPrint(2, "[???] You need to leave.")
        loop.delayPrint(3, "[???] I'm getting tired. Please leave.")
        loop.delayPrint(7, "[???] Alright, that's it.")
        time.sleep(2)"""
        # moves
        basicattack = Attack(damage = 5, energyCost = -17.5, name = "Basic Attack", isHealing = False)
        sliceattack = Attack(damage = 10, energyCost = 10, name = "Slice", isHealing = False)

        # characters/heroes
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

        """
        os.system("cls")
        
        loop.delayPrint(4, "[???] You have been defeated.")
        loop.delayPrint(1.5, "[???] Now leave.")
        time.sleep(2.5)
        loop.loadingScreen()
        os.system("cls")
        loop.delayPrint(3, "[???] Hello?")
        loop.delayPrint(2.5, "[???] Oh my, are you okay??")
        loop.delayPrint(2, "[???] Damn, you seem really bruised...")
        loop.delayPrint(2.5, "[???] Follow me, I'll get you some help!")
        os.system("cls")
        loop.delayPrint(3, "The unknown person drags you to a campsite . . .")
        os.system("cls")
        loop.delayPrint(5, "[???] What happened to you? You're in really bad shape...")
        loop.delayPrint(2, "[???] Don't worry, I know a guy who can help for things like this.")
        loop.delayPrint(3, "")
        loop.delayPrint(2.5, "[???] Oh! By the way, I'm Jade. Who might you be? ")
        loop.delayPrint(3, f"I'm {playerName}.")
        loop.delayPrint(2.5, "[Jade] I see. Strange name, but then again, you don't look like an normal, average guy.")
        loop.delayPrint(2.5, "[Jade] The others should be arriving soon... You never know though.")
        loop.delayPrint(3.5, "[Jade] The forest surrounding the area is filled with monsters, so they might be caught up with dealing with some of them.")
        loop.delayPrint(5, "...")
        loop.delayPrint(2.5, "[Jade] Now that I think about it, it has been a while since they've went out. I might have to look for them...")
        loop.delayPrint(4, "[Jade] Don't worry, though. You'll be in good hands sooner or later.")
        loop.delayPrint(2, "[Jade] Follow me. I'll go look for them.")
        loop.delayPrint(4.5, "Jade leads the way as she tries searching for her party.")
        loop.delayPrint(5, "Just then, the two of you hear a faint noise.")
        loop.delayPrint(3.5, "[Jade] Sounds like commotion. I wonder what's happening?")
        loop.delayPrint(2.5, "The two of you venture closer to the source of the noise...")
        loop.loadingScreen()
        os.system("cls")
        loop.delayPrint(3.5, "You see two individuals struggling with a particularly large foe...")
        loop.delayPrint(2, "[Jade] Shoot, I think that's them. Quick, let's help them out!")
        os.system("cls")"""
        
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
        yeOldeGnome = Enemy("Ye Olde Gnome", 200, 200, 30, {"Shrubbage", "Roll Over", "Stomp"}, "A")
        enemies.append(yeOldeGnome)
        
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
        loop.delayPrint(3.5, "[???] Damn, that guy was way tougher than usual...")
        loop.delayPrint(2.5, "[???] Exactly! Usually all we face are some little enemies, but this guy was really big!")
        loop.delayPrint(3.75, "[Jade] I'm glad you guys are all okay.")
        loop.delayPrint(2.5, f"{playerName}, this is Kelsey and Cashmere. Kelsey and Cashmere, {playerName}.")
        loop.delayPrint(3, "[Jade] I found this guy near our campsite looking horribly disheveled, and I wanted to see if you guys could do anything about it.")
        loop.delayPrint(2.5, "[Cashmere] Oh my... Of course!")
        loop.delayPrint(6.5, "Cashmere tends to your wounds. You haven't bothered to look down the entire time, apparently, because you didn't even notice you had wounds on you.")
        loop.delayPrint(2, "[Kelsey] That's only a temporary fix, though. We should probably head back to the campsite if we want to actually do something.")
        loop.delayPrint(1.5, f"[Jade] Yeah, we also have to decide what to do with {playerName}. ")
        loop.delayPrint(2, f"[Kelsey] Oh yeahhh! Where did you even come from, {playerName}?")
        loop.delayPrint(2.5, "Where did I come from? That's obvious! I came from")
        loop.delayPrint(2, "Uhhhhhh")
        loop.delayPrint(5, "...")
        loop.delayPrint(3.5, "I don't... remember...")
        loop.delayPrint(4, "[Cashmere] Uhh???? Alright then?? I guess we can take care of you for now...")
        loop.delayPrint(2.5, "[Jade] That's really strange... ")
        loop.delayPrint(2.5, "[Kelsey] When Cashmere was tending to your wounds, I noticed a strange mark on your forearm. Do any of you know what that is?")
        loop.delayPrint(3, "You look down, and lo and behold, there it is. A particularly strange mark is imbedded into your forearm, and there seems to be a strange pulsing emanating from it.")
        loop.delayPrint(2, "[Jade] Yikes.... We probably shouldn't touch that. What if it's dangerous?")
        loop.delayPrint(3.5, f"[Cashmere] Good point. Let's go. We'll figure out what to do with {playerName} eventually.")
        loop.delayPrint(1.5, "[Kelsey] I guess that settles it then? We just have another person now...?")
        loop.delayPrint(2.5, "[Jade] You say that as if we don't need the manpower...")
        loop.delayPrint(3.5, "[Cashmere] Come on, you guys, let's head back for now.")
        loop.delayPrint(4.5, "Now with a newfound group, you head to a campsite on the edge of the forest.")
        loop.loadingScreen()
        os.system("cls")
        loop.delayPrint(4, "[Kelsey] I can't WAIT for you to meet our campsite! It's got so much cool stuff and there's so much nature stuff and like there's - ")
        loop.delayPrint(1.5, "[Jade] Shut up, Kel. You're ruining the surprise.")
        loop.delayPrint(2.5, "[Kelsey] ??? Sorry I guess??? Excuse me for being excited about an accomplishment...")
        loop.delayPrint(2, f"[Jade] I'm not trying to play down our accomplishment, I'm just saying that MAYBE {playerName} might want to find out for themself...")
        loop.delayPrint(2.5, "[Kelsey] Well SORRY for slightly disrupting your routine, perfectionist...")
        loop.delayPrint(1.5, "[Jade] Are you actually serious right now")
        loop.delayPrint(4.5, "[Cashmere] Errrh... Guys, you might want to check this out...")
        loop.delayPrint(1.5, "[Kelsey] WHAT DO YOU MEAN 'are you actually serious right now' ?????")
        loop.delayPrint(2, "[Jade] WHAT I MEAN IS THAT MAYBE YOU DON'T HAVE TO BE SO IMPULSIVE ALL THE TIME????")
        loop.delayPrint(2.5, "[Cashmere] Guys -")
        loop.delayPrint(2.25, "[Kelsey] THERE IS NO WAY WE'RE GETTING INTO THIS RIGHT NOW IN FRONT OF THE NEW GUY")
        loop.delayPrint(2, "[Jade] OH YOU WANNA BRING THEM INTO THIS???")
        loop.delayPrint(1, "[Cashmere] THE CAMPSITE IS GONE YOU IDIOTS")
        time.sleep(0.25)
        print("[Jade] WHAT")
        print("[Kelsey] WHAT")
        loop.delayPrint(0.5, "WHAT???")
        loop.delayPrint(2, "Damn. Cashmere is right. The group's so-called 'campsite' seems to be nothing but a bunch of blankets and cloths now...")
        loop.delayPrint(1, "There's also some seemingly foreign markings in the ground. ")
        loop.delayPrint(2, "[Jade] Oh god oh god oh god oh god oh god")
        loop.delayPrint(2, "[Kelsey] Yall where is Clove?")
        loop.delayPrint(1.5, "Clove...? Must be another one of their troupe.")
        loop.delayPrint(2, "[Cashmere] Shoot, you're right... Clove is missing!")
        loop.delayPrint(3, "[Cashmere] I can't seem to find any sign of him anywhere... Maybe he's just wandered off?")
        loop.delayPrint(1, "[Jade] Clove wouldn't do that... It's not like them!")
        loop.delayPrint(1.5, "[Kelsey] OUSI;GH;AISDHG;ASDIGHAS;DLKHG well isn't this just the best day ever")
        loop.delayPrint(2.5, "[Cashmere] Calm down, you guys. We'll find him...")
        loop.delayPrint(1, "[Jade] How do you even know for sure???")
        loop.delayPrint(1.5, "[Cashmere] What, are we just going to give up on searching for him?")
        loop.delayPrint(1, "[Kelsey] He brings up a good point....")
        loop.delayPrint(2.5, "[Jade] I do NOT want to hear this from you right now Kelsey")
        loop.delayPrint(1.5, "[Cashmere] Calm down, everyone. Do you all remember the caves we discovered a while back near here?")
        loop.delayPrint(1, f"[Kelsey] {playerName} definitely wouldn't...")
        loop.delayPrint(1, "[Jade] NOT HIS POINT RIGHT NOW KEL")
        loop.delayPrint(1.5, "[Cashmere] What I was trying to say was that maybe we could start searching there?")
        loop.delayPrint(2.5, "[Kelsey] Alright, but it's going to be quite dangerous there...")
        loop.delayPrint(1, "[Cashmere] Clove could also be in danger.")
        loop.delayPrint(1.5, "[Jade] Come on, let's go already....")
        loop.delayPrint(2, "I guess we're going to the caves now?")
        loop.delayPrint(1, "None of them really asked about my opinion on this, but... whatever... it sounds important to them.")
        loop.delayprint(1, "I still have yet to figure out what the hell I'm doing here, though.")
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
        loop.delayPrint(1.5, "[Cashmere] Now's not the time to bicker, guys. Get ready to fight...")
        
        Ceres.currentHealth = 90
        Ceres.currentEnergy = 45
        Jade.currentHealth = 120
        Jade.currentEnergy = 50
        Kelsey.currentHealth = 75
        Kelsey.currentEnergy = 55
        Cashmere.currentHealth = 140
        Cashmere.currentEnergy = 75

        enemies.clear()
        voraciousSpider = Enemy("Voracious Spider", 80, 80, 20, {"String Shot", "Venom Shot", "Lunge"}, "A")
        undeadMiner = Enemy("Undead Miner", 110, 110, 15, {"Shovel Whack", "Shovel Smack"}, "B")
        bat = Enemy("Bat", 30, 30, 40, {"Nibble"}, "C")
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
        loop.delayPrint(2, "[Jash] I am not here to debate about specific details. Would you like to purchase items from me?")
        while True:
            shopOrNo = input("Buy items at Jash's store? Y/N ").strip().lower()        
            if shopOrNo not in ["y", "n", "yes", "no"]:
                loop.delayPrint(2.5, "[Jash] What? I didn't hear you... Try again, perhaps?")
            elif shopOrNo in ["y", "yes"]:
                loop.delayPrint(1.5, "[Jash] Excellent... excellent, excellent, excellent...")
                break
            elif shopOrNo in ["n", "no"]:
                loop.delayPrint(1, "[Jash] Oh... but I really want to sell stuff...")
            break

        player = inShop.Player(playerName, 500)
        strengthItem = inShop.Item("Strength Modifier", 40, 5)
        movesetConsumable00 = inShop.Item("Moveset Consumable 00", 350, 1)

        merchant = inShop.Merchant("Jash")
        merchant.add_item(strengthItem)
        merchant.add_item(movesetConsumable00)

        os.system("cls")
        merchant.list_items()
        while 屌你老母 == 1:
            boughtItem = input("Which item would you like to buy? ").strip()
            os.system('cls')
            boughtItemAmt = int(input("How many would you like to buy? "))
            os.system('cls')
            merchant.sell_item(player, boughtItem, boughtItemAmt)

            print(player)
            print(merchant)
            
            while True:
                屌你老母 = input("Continue? Y/N ").strip().lower()
                if 屌你老母 == "y":
                    屌你老母 = 1
                    os.system('cls')
                    merchant.list_items()
                    break
                elif 屌你老母 == "n":
                    break
                print("Sorry, I couldn't get that. Try again.")
                break

            break

        loop.delayPrint(1.5, "[Jash] Hehe... pleasure doing business...")
        time.sleep(1.5)
        input("Press Enter to open the inventory. ")
        loop.delayPrint(3, player)
        while True:
            useItemsInInventory = input("Would you like to use anything in the inventory? Y/N ").strip().lower()        
            if useItemsInInventory not in ["y", "n", "yes", "no"]:
                loop.delayPrint(2.5, "Invalid input. Try again. ")
            elif useItemsInInventory in ["y", "yes"]:
                os.system("cls")
                time.sleep(1, player)
                while True: 
                    usedItem = input("What would you like to use? (Case Sensitive)").strip()
                    if usedItem not in ["Strength Modifier", "Moveset Consumable 00"]:
                        time.sleep(1)
                        input("Invalid selection. Press Enter to try again.")
                    elif usedItem == "Strength Modifier":
                        loop.delayPrint(1.5, f"Strength Modifier - Buffs all heroes' stats for the next battle.")
                        while True:
                            useOrNo = input("Use item? Y/N ").strip().lower()
                            if useOrNo not in ["y", "yes", "n", "no"]:
                                time.sleep(1)
                                input("Invalid selection. Press Enter to try again. ")
                            elif useOrNo in ["y", "yes"]:
                                loop.delayPrint(1.5, "Successfully applied the Strength Modifier. ")
                                currentLevel = 3
                                break
                            elif useOrNo in ["n", "no"]:
                                input("Press Enter to go back. ")
                                break
                            break
                    elif usedItem == "Moveset Consumable 00":
                        loop.delayPrint(1.5, f"Moveset Consumable 00 - Appends a new item to {playerName}'s moveset. ")
                        while True:
                            useOrNo = input("Use item? Y/N ").strip().lower()
                            if useOrNo not in ["y", "yes", "n", "no"]:
                                time.sleep(1)
                                input("Invalid selection. Press Enter to try again. ")
                            elif useOrNo in ["y", "yes"]:
                                loop.delayPrint(1.5, "Successfully applied the Moveset Consumable 00. ")
                                trick = Attack(50, 50, "Trick", isHealing = False)
                                Ceres = Hero(playerName, 105, 105, 50, 100, 7.5, currentLevel, [("Basic Attack", "A", basicattack), ("Slice", "B", sliceattack), ("Stab", "C", stab), ("Trick", "D", trick)], "A")
                                break
                            elif useOrNo in ["n", "no"]:
                                input("Press Enter to go back. ")
                                break
                            break
                    continueyesorno = input("Continue? Y/N ").strip().lower()
                    if continueyesorno not in ["y", "yes", "n", "no"]:
                        time.sleep(1)
                        input("Invalid Selection. Try again.")
                        continue
                    elif continueyesorno in ["n", "no"]:
                        loop.delayPrint(1.5, "Exiting . . . ")
                        break
                    elif continueyesorno in ["y", "yes"]:
                        continue
                    break
                break
            elif useItemsInInventory in ["n", "no"]:
                loop.delayPrint(1, "Very well. Closing inventory...")
            break
        loop.loadingScreen()
        os.system("cls")
        loop.delayPrint(1, "And within a fraction of a second, Jash disappears...")
      

    def delayPrint(delaySeconds, printString):
        time.sleep(delaySeconds)
        print(printString)

loop.mainLoop()