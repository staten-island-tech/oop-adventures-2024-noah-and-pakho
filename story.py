import os
import time
import random
import combat

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

def combatLoop():
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
    elif startingOption == "a":
        loop.initializeGame()
        os.system("cls")
        print("[???] Hello!")
        time.sleep(1.5)
        print("[???] You certainly look very strange. Who are you?")
        time.sleep(2)
        print("Who are you?")
        playerName = input().strip().lower()
        break