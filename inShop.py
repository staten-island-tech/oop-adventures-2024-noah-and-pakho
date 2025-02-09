import os

class Item:
    def __init__(self, name, price, quantity, position):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.position = position

    def __str__(self):
        return f"{self.name} (Price: {self.price}, Quantity: {self.quantity})"

    def is_available(self):
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
            print(f"{item} [{item.position}]")

    def sell_item(self, player, itemName, quantity=1):
        if itemName not in self.inventory:
            print(f"{itemName} is not available at this shop.")
            return False

        item = self.inventory[itemName]
        if not item.is_available() or item.quantity < quantity:
            print(f"Sorry, we don't have enough {itemName} in stock.")
            return False

        totalCost = item.price * quantity
        if player.monies < totalCost:
            print(f"{player.name} doesn't have enough monies.")
            return False

        player.monies -= totalCost
        player.add_item(Item(itemName, item.price, quantity, item.position))
        item.quantity -= quantity
        if item.quantity <= 0:
            del self.inventory[itemName]
        print(f"{player.name} bought {quantity} {itemName}(s) for {totalCost} monies.")
        print(f"{player.name} has {player.monies} monies left.")
        return True
    
    def __str__(self):
        return f"{self.name} (Items: {', '.join(self.inventory.keys())})"


class Player:
    def __init__(self, name, monies):
        self.name = name
        self.monies = monies
        self.inventory = {}

    def __str__(self):
        return f"{self.name} (Monies: {self.monies}, Inventory: {', '.join(self.inventory.keys())})"

    def add_item(self, item):
        if item.name in self.inventory:
            self.inventory[item.name].quantity += item.quantity
        else:
            self.inventory[item.name] = item
    
    def use_item(self, item_name):
        if item_name in self.inventory:
            item = self.inventory[item_name]
            item.quantity -= 1
            if item.quantity <= 0:
                del self.inventory[item_name]
            print(f"{self.name} used {item_name}.")
            return True
        else:
            print(f"{item_name} is not in your inventory.")
            return False

class Game:
    def inShop():
        os.system('cls')
        global 屌你老母
        屌你老母 = True
        # create player
        player = Player("Test", 500)
        # items 
        heals = Item("Test Healing Item", 50, 1)
        moveitem = Item("Test Moveset Consumable", 200, 1)

        merchant = Merchant("Shopkeep")
        merchant.add_item(heals)
        merchant.add_item(moveitem)

        merchant.list_items()
        while 屌你老母:
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
                    屌你老母 = True
                    os.system('cls')
                    merchant.list_items()
                    break
                elif 屌你老母 == "n":
                    break
                print("Sorry, I couldn't get that. Try again.")

"""and then here theres gonna be a function to lead into the other after you exit the shop"""
