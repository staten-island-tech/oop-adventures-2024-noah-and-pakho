import os
import time
import random
import combat

currentLevel = 1
randomTip = random.randint(1, 5)
class loopLogic:
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
        loopLogic.tips()
        time.sleep(1.5)
        os.system("cls")
        print("Loading .")
        loopLogic.tips()
        time.sleep(1.5)
        os.system("cls")
        print("Loading . .")
        loopLogic.tips()
        time.sleep(1.5)
        os.system("cls")
        print("Loading . . .")
        loopLogic.tips()
        time.sleep(1.5)
        os.system("cls")
        print("Loading . . . .")
        loopLogic.tips()
        time.sleep(1.5)
        os.system("cls")
        print("Loading . . .")
        loopLogic.tips()
        time.sleep(1.5)
        os.system("cls")
        print("Loading . .")
        loopLogic.tips()
        time.sleep(1.5)
        os.system("cls")
        print("Loading .")
        loopLogic.tips()
        time.sleep(1.5)
        os.system("cls")
        input("Done! Press Enter to continue. ")

    def mainloopLogic():
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
                loopLogic.initializeGame()

                while True:
                    combat.game.heroSelect()

                    if combat.game.selectedHero:
                        combat.game.combatTurn()
            elif startingOption == "b":
                os.system("cls")
                input("Press Enter to start the combat simulation. ")

                while True:
                    combat.game.heroSelect()

                    if combat.game.selectedHero:
                        combat.game.combatTurn()
    def delayPrint(delaySeconds, printString):
        time.sleep(delaySeconds)
        print(printString)

def combatloopLogic():
    while True:
        combat.game.heroSelect()
        if combat.game.selectedHero:
            combat.game.combatTurn()

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
    break

while True:
    loopLogic.initializeGame()
    os.system("cls")
    print("")
    os.system("cls")
    loopLogic.delayPrint(1.5, "[???] Hello there.")
    loopLogic.delayPrint(2, "[???] What are you doing here?")
    loopLogic.delayPrint(3, "What...?")
    loopLogic.delayPrint(2, "[???] Who are you? What are you doing here?")
    loopLogic.delayPrint(3, "[???] Are you there?")
    time.sleep(2)
    print("Good question... Who am I?")
    time.sleep(5)
    playerName = input("Who are you? ").strip()
    if not playerName:
        loopLogic.delayPrint(2, "[???] Sorry, I didn't get that. Say that again?")
    else:
        break
    break

loopLogic.delayPrint(1, f"I am {playerName}.")
loopLogic.delayPrint(3.5, "[???] Hm.")
loopLogic.delayPrint(2, f"[???] {playerName}?")
loopLogic.delayPrint(2, "[???] That's a horrible name.")
loopLogic.delayPrint(1, "[???] Whatever... You seem lost. ")
loopLogic.delayPrint(1.5, "[???] Confused, perhaps...?")
loopLogic.delayPrint(2, f"[???] Let me explain: Your name is {playerName}, apparently, and you are in my temple.")
loopLogic.delayPrint(4, "[???] I would be way more aggressive, but I'll give you the benefit of the doubt.")
loopLogic.delayPrint(2.5, "[???] I'm pretty busy right now, so I'm going to kindly ask you to leave.")
loopLogic.delayPrint(4, "...")
loopLogic.delayPrint(1.5, "Huh?")
loopLogic.delayPrint(4, "[???] What do you mean, 'huh' ??")
loopLogic.delayPrint(2, "[???] You need to leave.")
loopLogic.delayPrint(3, "[???] I'm getting tired. Please leave.")
loopLogic.delayPrint(7, "[???] Alright that's it.")
"""
basicattack = combat.Attack(damage = 5, energyCost = -17.5, name = "Basic Attack", isHealing = False)
sliceattack = combat.Attack(damage = 10, energyCost = 10, name = "Slice", isHealing = False)

Ceres = combat.Hero(playerName, 90, 90, 25, 50, 8, currentLevel, [("Basic Attack", "A", basicattack), ("Slice", "B", sliceattack)], "A")
heroes = [Ceres]

Zol = combat.Enemy("???", 10000, 10000, 10000, {"Demolish"}, "A")
enemies = [Zol]

game = combat.Game(heroes, enemies)

while True:
    combat.game.heroSelect()
    if combat.game.selectedHero:
        combat.game.combatTurn()
    """