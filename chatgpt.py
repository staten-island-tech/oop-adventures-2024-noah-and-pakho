import os

class Hero:
    def __init__(self, name, health, energy, moveset, position):
        self.name = name
        self.health = health
        self.energy = energy
        self.moveset = moveset
        self.position = position
    
    def displayStats(self):
        print(f"Health: {self.health}")
        print(f"Energy: {self.energy}")
        
        # Display moveset horizontally with commas between them
        moves = [move.name for move in self.moveset]  # Get the names of the moves
        print("Moveset:", ", ".join(moves))  # Join the names with commas and print horizontally

class Enemy:
    def __init__(self, name, health, moveset, position):
        self.name = name
        self.health = health
        self.moveset = moveset
        self.position = position
    
    def displayEnemyStats(self):
        print(f"Health: {self.health}")
        print(f"Moveset: {self.moveset}")

class Attack:
    def __init__(self, name, energy_cost, damage):
        self.name = name
        self.energy_cost = energy_cost
        self.damage = damage
    
    def __repr__(self):
        return f"{self.name} (Energy Cost: {self.energy_cost}, Damage: {self.damage})"

class Game:
    def __init__(self, heroes, enemies):
        self.heroes = heroes
        self.selectedHero = None
        self.selectedEnemy = None
        self.enemies = enemies
    
    def displayParty(self):
        os.system("cls")  # uses a list to display information horizontally
        hero_names = []
        hero_health = []
        hero_energy = []

        for hero in self.heroes:  # adds the hero stats to the list
            hero_names.append(f"{hero.name} [{hero.position}]")
            hero_health.append(f"Health: {hero.health}")
            hero_energy.append(f"Energy: {hero.energy}")
        
        # Print heroes' names, health, and energy
        print("    ".join(hero_names))
        print("    ".join(hero_health))
        print("    ".join(hero_energy))
        print("\n")
    
    def heroSelect(self):
        self.displayParty()
        selectedPosition = input("Please select a character by entering a letter: ")
        for hero in self.heroes:
            if selectedPosition == hero.position:
                os.system("cls")
                self.selectedHero = hero
                print(f"Currently selected Hero: {self.selectedHero.name}")
                self.selectedHero.displayStats()
                input("Please press Enter to continue. ")
    
    def displayEnemyParty(self):
        os.system("cls")
        # Display enemies horizontally with health
        enemy_names = []
        enemy_health = []

        for enemy in self.enemies:
            enemy_names.append(f"{enemy.name} [{enemy.position}]")
            enemy_health.append(f"Health: {enemy.health}")
        
        # Print enemy names and health
        print("    ".join(enemy_names))
        print("    ".join(enemy_health))
        print(f"\nCurrently selected Hero: {self.selectedHero.name}")
    
    def enemySelect(self):
        self.displayEnemyParty()
        selectedEnemyPosition = input("Please select the targeted enemy by entering a letter: ")
        for enemy in self.enemies:
            if selectedEnemyPosition == enemy.position:
                os.system("cls")
                self.selectedEnemy = enemy
                print(f"Currently selected Hero: {self.selectedHero.name}")
                print(" ")
                print(f"Targeted Enemy: {enemy.name}")
                enemy.displayEnemyStats()
                input("Please press Enter to continue. ")
    
    def displayMoveset(self):
        os.system("cls")
        # Display hero's moveset with energy cost and damage
        move_names = []
        move_costs = []
        move_damage = []

        for move in self.selectedHero.moveset:
            move_names.append(move.name)
            move_costs.append(f"Energy Cost: {move.energy_cost}")
            move_damage.append(f"Damage: {move.damage}")
        
        # Print moveset information
        for i in range(len(move_names)):
            print(f"{move_names[i]} [{chr(65 + i)}]    {move_costs[i]}    {move_damage[i]}")
    
    def confirmSelection(self):
        while True:
            # Display the selected hero and selected enemy's stats side by side
            os.system("cls")
            print(f"Attacker: {self.selectedHero.name}    Enemy: {self.selectedEnemy.name}")
            print(f"Health: {self.selectedHero.health}            Health: {self.selectedEnemy.health}")
            print(f"Energy: {self.selectedHero.energy}")
            # Ask for confirmation or go back option
            confirmation = input("Type A to confirm your selections and proceed.\nType B to go back and reselect your hero and enemy: ").upper()
            
            if confirmation == 'A':
                print("Success.")
                break  # Exit the loop after confirmation
            elif confirmation == 'B':
                print("Reselecting your hero and enemy.")
                self.heroSelect()  # Reselect hero
                self.enemySelect()  # Reselect enemy
                break  # Exit loop after reselecting
            else:
                # Invalid input handling
                os.system("cls")  # Clear the console
                self.displaySelectionStats()  # Re-display stats
                print("Not a valid option. Please select A or B.")

    def displaySelectionStats(self):
        # Re-display the selected hero and selected enemy's stats side by side
        print(f"Attacker: {self.selectedHero.name}    Enemy: {self.selectedEnemy.name}")
        print(f"Health: {self.selectedHero.health}            Health: {self.selectedEnemy.health}")
        print(f"Energy: {self.selectedHero.energy}")

# Create moves for heroes
shoulder_bash = Attack("Shoulder Bash", 20, 10)
toss = Attack("Toss", 40, 25)
jab = Attack("Jab", 15, 8)
kick = Attack("Kick", 25, 20)
cook = Attack("Cook", 30, 15)
slam = Attack("Slam", 35, 22)

# Create heroes
Aubrey = Hero("Aubrey", 100, 100, [shoulder_bash, toss], "A")
Kelsey = Hero("Kelsey", 100, 100, [jab, kick], "B")
Cashmere = Hero("Cashmere", 100, 100, [cook, kick], "C")
Omari = Hero("Omari", 100, 100, [shoulder_bash, slam], "D")
heroes = [Aubrey, Kelsey, Cashmere, Omari]

# Create enemies
Slime = Enemy("Slime", 50, {"Goo'd", "Acid Spit"}, "A")
Goblin = Enemy("Goblin", 75, {"Bash", "Slash"}, "B")
Skeleton = Enemy("Skeleton", 100, {"Slice", "Shoot"}, "C")
enemies = [Slime, Goblin, Skeleton]

game = Game(heroes, enemies)

# Simulate the selection process
game.heroSelect()
game.enemySelect()
game.confirmSelection()
