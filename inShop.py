import os
import test

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (Price: {self.price}, Quantity: {self.quantity})"

    def is_available(self):
        # check if available for purchase
        return self.quantity > 0


class Merchant:
    def __init__(self, name):
        self.name = name
        self.inventory = {}

    def add_item(self, item):
        if item.name in self.inventory:
            self.inventory[item.name].quantity += item.quantity
        else:
            self.inventory[item.name] = item

    def list_items(self):
        print(f"Items for sale by {self.name}:")
        for item in self.inventory.values():
            print(item)

    def sell_item(self, player, itemName, quantity=1):
        if itemName not in self.inventory:
            print(f"{itemName} is not available at this shop.")
            return False

        item = self.inventory[itemName]
        if not item.is_available() or item.quantity < quantity:
            print(f"Sorry, we don't have enough {itemName} in stock.")
            return False

        totalCost = item.price * quantity
        if player.gold < totalCost:
            print(f"{player.name} doesn't have enough gold.")
            return False

        player.gold -= totalCost
        player.add_item(Item(itemName, item.price, quantity))
        item.quantity -= quantity
        if item.quantity <= 0:
            del self.inventory[itemName]
        print(f"{player.name} bought {quantity} {itemName}(s) for {totalCost} gold.")
        print(f"{player.name} has {player.gold} gold left.")
        return True
    
    def __str__(self):
        return f"{self.name} (Items: {', '.join(self.inventory.keys())})"


class Player:
    def __init__(self, name, gold):
        self.name = name
        self.gold = gold
        self.inventory = {}

    def __str__(self):
        return f"{self.name} (Gold: {self.gold}, Inventory: {', '.join(self.inventory.keys())})"

    def add_item(self, item):
        if item.name in self.inventory:
            self.inventory[item.name].quantity += item.quantity
        else:
            self.inventory[item.name] = item

class Game:
    def inShop():
        os.system('cls')
        屌你老母 = 1
        # create player
        player = Player("Test", 500)
        # items 
        heals = Item("Test Healing Item", 50, 1)
        moveitem = Item("Test Moveset Consumable", 200, 1)

        merchant = Merchant("Shopkeep")
        merchant.add_item(heals)
        merchant.add_item(moveitem)

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

"""and then here theres gonna be a function to lead into the other after you exit the shop"""

Game.inShop()
os.system('cls')