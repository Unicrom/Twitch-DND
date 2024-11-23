from other.saveFile import readFileJSON


class Item:
    equippedRef = [
        "unequipped",
        "weapon",
        "head",
        "chest",
        "legs",
        "feet",
        "necklace",
        "bracelet",
        "belt",
    ]  # what each number for the equipped var means.

    def __init__(self, item, itemType, subtype, amount, level=1, equipped=0):
        self.item = item
        self.type = itemType
        self.subtype = subtype
        self.amount = amount
        self.level = level
        self.equipped = equipped

    def updateAmount(self, change):
        """Increases/Decreases amount of item"""
        self.amount += change

    def toJSON(self):
        """Returns a DICT that storing this items data"""
        itemJSON = {
            "item": self.item,
            "type": self.type,
            "subtype": self.subtype,
            "amount": self.amount,
            "level": self.level,
            "equipped": self.equipped,
        }
        return itemJSON

    def getInfo(self):
        """Returns a list of item information
        \nList Structure: [item, display, amount, level, equipped, type, rarity, description]
        """
        itemData = readFileJSON("data/other/items.json")

        display = itemData[self.type][self.subtype][self.item]["display"]
        rarity = itemData[self.type][self.subtype][self.item]["rarity"]
        desc = itemData[self.type][self.subtype][self.item]["desc"]

        return [
            self.item,
            display,
            self.amount,
            self.level,
            self.equipped,
            self.type,
            self.subtype,
            rarity,
            desc,
        ]
