import os
import random
import time
import inShop

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
        
        loop.loadingScreen()
        os.system("cls")
        
        time.sleep(2)
        print("Good question... Who am I?")
        time.sleep(5)
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
        
        os.system("cls")
        
        loop.loadingScreen()
        os.system("cls")

        input("Entering Jash's shop. Press Enter to proceed. ")

        player = inShop.Player(playerName, 500)
        strengthItem = inShop.Item("Strength Modifier", 40, 1)
        movesetConsumable00 = inShop.Item("Moveset Consumable 00", 350, 1)

        merchant = inShop.Merchant("Jash")
        merchant.add_item(strengthItem)
        merchant.add_item(movesetConsumable00)

        os.system("cls")
        merchant.list_items()
        while True:
            boughtItem = input("Which item would you like to buy? ").strip()

            if boughtItem not in [item.name for item in merchant.inventory.values()]:
                input("Invalid input. Press enter to try again. ")
                continue

            boughtItemAmt = int(input("How many would you like to buy? "))
            os.system("cls")
            try:
                boughtItemAmt = int(boughtItemAmt)
                if boughtItemAmt <= 0:
                    input("Quantity must be greater than 0. Press Enter to continue. ")
                    continue
            except ValueError:
                input("Invalid quantity. Press Enter to try again. ")
                continue

            os.system('cls')
            merchant.sell_item(player, boughtItem, boughtItemAmt)

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
        loop.delayPrint(1.5, "[Jash] Hehe... pleasure doing business...")
        time.sleep(1.5)
        input("Press Enter to open the inventory. ")
        time.sleep(3)
        os.system("cls")
        print(player)
        while True:
            if not player.inventory:
                loop.delayPrint(1.5, "Your inventory is empty. Nothing to use. ")
                input("Press Enter to continue. ")
                break
            useItemsInInventory = input("Would you like to use anything in the inventory? Y/N ").strip().lower()        
            if useItemsInInventory not in ["y", "n", "yes", "no"]:
                loop.delayPrint(2.5, "Invalid input. Try again. ")
            elif useItemsInInventory in ["y", "yes"]:
                os.system("cls")
                loop.delayPrint(1, player)
                while True: 
                    os.system("cls")
                    print(player)
                    if not player.inventory:
                        break
                    else:
                        usedItem = input("What would you like to use? (Case Sensitive) ").strip()
                        if usedItem not in player.inventory:
                            time.sleep(1)
                            input("Invalid selection. Press Enter to try again.")
                            continue
                        elif usedItem == "Strength Modifier":
                            loop.delayPrint(1.5, f"Strength Modifier - Buffs all heroes' stats for the next battle.")
                            while True:
                                useOrNo = input("Use item? Y/N ").strip().lower()
                                if useOrNo not in ["y", "yes", "n", "no"]:
                                    time.sleep(1)
                                    input("Invalid selection. Press Enter to try again. ")
                                elif useOrNo in ["y", "yes"]:
                                    loop.delayPrint(1.5, "Successfully applied the Strength Modifier. ")
                                    player.use_item("Strength Modifier")
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
                                    player.use_item("Moveset Consumable 00")
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
                            os.system("cls")
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