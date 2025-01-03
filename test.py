import os

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (Price: {self.price}, Quantity: {self.quantity})"

    def is_available(self):
        """Checks if the item is available for purchase."""
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

    def sell_item(self, player, item_name, quantity=1):
        if item_name not in self.inventory:
            print(f"{item_name} is not available at this shop.")
            return False

        item = self.inventory[item_name]
        if not item.is_available() or item.quantity < quantity:
            print(f"Sorry, we don't have enough {item_name} in stock.")
            return False

        total_cost = item.price * quantity
        if player.gold < total_cost:
            print(f"{player.name} doesn't have enough gold.")
            return False

        player.gold -= total_cost
        player.add_item(Item(item_name, item.price, quantity))
        item.quantity -= quantity
        print(f"{player.name} bought {quantity} {item_name}(s) for {total_cost} gold.")
        print(f"{player.name} has {player.gold} gold left.")
        return True
    
    def __str__(self):
        return f"{self.name} (Items: {', '.join(self.inventory.keys())})"


class Player:
    def __init__(self, name, gold=100):
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
# Example Usage:
while True:
    # Create some items
    sword = Item("Sword", 50, 10)
    shield = Item("Shield", 40, 5)
    testpotion = Item("Test Bucket Please Ignore", 200, 2)

    # Create a merchant and add items to their inventory
    merchant = Merchant("Shopkeep")
    merchant.add_item(sword)
    merchant.add_item(shield)
    merchant.add_item(testpotion)

    # Create a player
    player = Player("PENI!", 500)

    # List available items for sale
    merchant.list_items()

    # Player buys some items from the merchant
    boughtItem = input("Which item would you like to buy? ").strip()
    boughtItemAmt = int(input("How many would you like to buy? "))
    merchant.sell_item(player, boughtItem, boughtItemAmt)

    # Show updated player and merchant status
    print(player)
    print(merchant)