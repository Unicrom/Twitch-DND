from items.item import Item


class Inventory:
    """Item Types: Weapon, Armor, Accessory, Crafting, Special"""

    def __init__(self):
        # The inventory storage: 5 different item types.
        self.items = []

    def itemsFromJSON(self, JSON):
        """Loops through JSON and adds each item to inventory"""
        for item in JSON:
            self.addItemFull(*item.values())

    # def addItem(self, item, amount, level):
    #     """Adds and item without needing to specify item type"""
    #     itemType = self.itemData[item]["type"]
    #     self.addItemFull(item, itemType, subtype, amount, level)

    def addItemFull(self, itemName, itemType, subtype, amount, level=1, equipped=0):
        """Adds and item to inventory. Requires all of the items info"""
        for item in self.items:  # Checks if item is already in inventory
            if not item.item == itemName:
                continue
            if not item.level == level:
                continue
            # If item already exists, increases the amount of said item.
            item.updateAmount(amount)
            return
        # If item does not exist, adds the item.
        self.items.append(Item(itemName, itemType, subtype, amount, level, equipped))

    def toJSON(self):
        """Returns a JSON version of the inventory"""
        inventoryJSON = []
        for type in self.items.values():
            for item in type:
                inventoryJSON.append(item.toJSON())
        return inventoryJSON

    def getItems(self, other=["item"]):
        """Returns all of the elements of a certain type. "Other" contains what information to return"""
        itemInfoRef = [
            "item",
            "display",
            "amount",
            "level",
            "equipped",
            "type",
            "rarity",
            "description",
        ]
        inventory = []
        specInfo = [itemInfoRef.index(i) for i in other]

        for item in self.items:
            itemInfo = [item.getInfo()[index] for index in specInfo]
            inventory.append(itemInfo)

        return inventory
