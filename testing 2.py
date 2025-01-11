import os
import random

class Hero:  # class for your characters
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
    
    def displayStats(self):  # displays a character's stats
        print(f"Name: {self.name}")
        print(f"Health: {self.currentHealth} / {self.maxHealth}")
        print(f"Energy: {self.currentEnergy} / {self.maxEnergy}")
        print(f"Moveset: {[move[0] for move in self.moveset]}")

    def regenerateEnergy(self):
        """Regenerate energy at the start of each turn, capped at maxEnergy."""
        self.currentEnergy += self.energyRegen
        if self.currentEnergy > self.maxEnergy:
            self.currentEnergy = self.maxEnergy


class Enemy:  # a class for enemies you fight against
    def __init__(self, name, currentHealth, maxHealth, strength, moveset, position):
        self.name = name
        self.currentHealth = currentHealth
        self.maxHealth = maxHealth
        self.strength = strength
        self.moveset = moveset
        self.position = position
    
    def displayEnemyStats(self):  # displays an enemy's stats
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
    def __init__(self, damage, energyCost, name="Unnamed Attack"):
        self.damage = damage
        self.energyCost = energyCost
        self.name = name

    def __str__(self):
        return self.name


class Game:
    def __init__(self, heroes, enemies):  # every instance of game will already have the list of heroes & enemies.
        self.heroes = heroes
        self.enemies = enemies
        self.selectedHero = None
        self.selectedEnemy = None  # this & the above lines are used for functions below.

    def displayParty(self):
        os.system("cls")
        for hero in self.heroes:  # loop that iterates through the list of heroes and displays each hero's stats
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
        for enemy in aliveEnemies:  # loop that iterates through list of enemies
            print(f"Name: {enemy.name} [{enemy.position}]")
            print(f"Health: {enemy.currentHealth}")
        print(" ")
        print(f"Selected Hero: {self.selectedHero.name}")  # reminder that shows your selected hero

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

            if not selectedEnemyPosition:  # same logic present in hero select
                input("Invalid position selected. Press enter to retry. ")
                os.system("cls")
                continue

            for enemy in aliveEnemies:
                if selectedEnemyPosition == enemy.position:
                    os.system("cls")
                    self.selectedEnemy = enemy
                    return
            input("Invalid enemy position selected. Press enter to retry. ")  # the reason why enemies arent printed when an invalid position is selected is here.
            os.system("cls")

    def displayMoveset(self):
        os.system("cls")
        print(f"{self.selectedHero.name} is attacking {self.selectedEnemy.name}!")  # tells you which hero is attacking which enemy
        print(" ")
        print(f"{self.selectedHero.name}'s Moveset:")  # reminder of who's moveset you're looking at
        for move, letter, attack in self.selectedHero.moveset:
            if move:
                print(f"{move} [{letter}] (Cost: {attack.energyCost} Energy, Damage: {attack.damage})")
        
        # If the hero has full energy, give the option to use the ultimate attack
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
                        if self.selectedHero.currentEnergy >= attack.energyCost:  # Ensure the hero has enough energy
                            self.selectedHero.currentEnergy -= attack.energyCost
                            return attack
                        else:
                            input("Not enough energy for that attack. Press Enter to retry.")
                            os.system("cls")
            elif selectedMovePosition == 'U' and self.selectedHero.currentEnergy == self.selectedHero.maxEnergy:
                # If 'U' is pressed and energy is full, unleash ultimate attack
                self.ultimateAttack()
                return None  # Return None as we've already used the ultimate attack
            else:
                input("Invalid move selection. Press Enter to retry. ")
                os.system("cls")

    def combatTurn(self):
        for hero in self.heroes:  # This creates the hero cycle
            if hero.currentHealth > 0:
                self.selectedHero = hero
                print(f"{self.selectedHero.name}'s turn:")

                # Regenerate energy before the turn
                self.selectedHero.regenerateEnergy()

                # Select the enemy for the hero to target
                self.enemySelect()  # Only one call here

                if self.selectedEnemy:  # Proceed if an enemy was selected
                    selectedMove = self.moveSelect()
                    if selectedMove is None:  # If ultimate attack was used, skip the rest of this hero's turn
                        continue

                    os.system("cls")
                    print(f"{self.selectedHero.name} uses {selectedMove} on {self.selectedEnemy.name}!")

                    damage = selectedMove.damage + (self.selectedHero.level * 2)
                    self.selectedEnemy.currentHealth -= damage
                    print(f"{self.selectedHero.name} dealt {damage} damage to {self.selectedEnemy.name}! ({self.selectedEnemy.currentHealth} / {self.selectedEnemy.maxHealth})")
                    input("Press Enter to continue. ")

                    if self.selectedEnemy.currentHealth <= 0:
                        self.selectedEnemy.currentHealth = 0
                        print(f"{self.selectedEnemy.name} has been defeated!")
                        self.selectedEnemy = None  # Make sure this is None when defeated

                if all(enemy.currentHealth <= 0 for enemy in self.enemies):
                    print("All enemies have been defeated!")
                    break  # End the turn if all enemies are dead

        # At this point, we need to ensure that enemies who are still alive take their turns
        if any(enemy.currentHealth > 0 for enemy in self.enemies):  # Check if there are still alive enemies
            os.system("cls")
            print("Enemy's turn!")
            aliveEnemies = [enemy for enemy in self.enemies if enemy.currentHealth > 0]
            for enemy in aliveEnemies:
                enemy.takeTurn(self.heroes)  # Let enemies take their turn

            # Check if all heroes are defeated
            if all(hero.currentHealth == 0 for hero in self.heroes):
                print("All heroes have been defeated! Game Over.")
                input("Press Enter to exit.")
                return

    def ultimateAttack(self):
        """Perform the ultimate attack, using all of the hero's energy."""
        print(f"{self.selectedHero.name} unleashes their Ultimate Attack!")
        # For simplicity, ultimate attack will deal a high amount of damage
        ultimateDamage = self.selectedHero.maxEnergy * 2
        if self.selectedEnemy:
            self.selectedEnemy.currentHealth -= ultimateDamage
            print(f"{self.selectedHero.name} dealt {ultimateDamage} damage to {self.selectedEnemy.name}! ({self.selectedEnemy.currentHealth} / {self.selectedEnemy.maxHealth})")
            self.selectedHero.currentEnergy = 0  # Use up all energy after ultimate attack
        input("Press Enter to continue.")


def masterLoop():
    while True:
        game.heroSelect()

        if game.selectedHero:
            game.enemySelect()
            if game.selectedEnemy:
                game.combatTurn()

                if not game.aliveEnemies:
                    break
                continue


# moves
shoulderBash = Attack(damage = 17, energyCost=15, name="Shoulder Bash")
uppercut = Attack(damage=12, energyCost=10, name="Uppercut")
toss = Attack(damage=20, energyCost=25, name="Toss")
jab = Attack(damage=8, energyCost=8, name="Jab")
dropKick = Attack(damage=13, energyCost=13, name="Drop Kick")
whack = Attack(damage=5, energyCost=1, name="Whack")
cook = Attack(damage=1, energyCost=15, name="Cook")
study = Attack(damage=0, energyCost=10, name="Study")
testmove = Attack(damage=999, energyCost=0, name="Test")
basicattack = Attack(damage = 5, energyCost = -17.5, name = "Basic Attack")

# characters/heroes
Jade = Hero("Jade", 110, 110, 55, 110, 10, 1, [("Shoulder Bash", "A", shoulderBash), ("Uppercut", "B", uppercut), ("Toss", "C", toss), ("Basic Attack", "D", basicattack)], "A")
Kelsey = Hero("Kelsey", 80, 80, 45, 90, 8, 1, [("Jab", "A", jab), ("Drop Kick", "B", dropKick), ("Basic Attack", "C", basicattack)], "B")
Cashmere = Hero("Cashmere", 100, 100, 45, 90, 7, 1, [("Cook", "A", cook), ("Whack", "B", whack), ("Basic Attack", "C", basicattack)], "C")
Ceres = Hero("Ceres", 90, 90, 50, 50, 8, 1, [("Shoulder Bash", "A", shoulderBash), ("Study", "B", study), ("Test", "C", testmove), ("Basic Attack", "D", basicattack)], "D")
heroes = [Jade, Kelsey, Cashmere, Ceres]

# enemies
Slime = Enemy("Slime", 25, 25, 35, {"Goo'd", "Acid Spit"}, "A")
Goblin = Enemy("Goblin", 75, 75, 5, {"Bash"}, "B")
Skeleton = Enemy("Skeleton", 100, 100, 10, {"Slice", "Shoot"}, "C")
enemies = [Slime, Goblin, Skeleton]

game = Game(heroes, enemies)

os.system("cls")
input("Press Enter to start the combat simulation. ")

while True:
    game.heroSelect()

    if game.selectedHero:
        game.combatTurn()

# bugs:
    
# changes:
    # when selecting an enemy, the hero you are attacking with is displayed.
    # fixed bug where if an invalid enemy position is selected, enemy names / stats won't be printed again.
    # made it so that hero health is displayed when enemies deal damage

# idea:
    # one of the characters will be able to generate energy past their max, meaning they have infinite energy.
    # one of their moves will be a "wait" move that costs zero energy, but does not deal damage.
    # another move will be a move that does damage based on all of your energy past a certain amount
    # 0 + 1(energy past maxEnergy) * (strength / 5)