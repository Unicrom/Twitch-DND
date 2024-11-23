import other.saveFile as saveFile
from items.inventory import Inventory


class Character:
    defaultSave = saveFile.readFileJSON("data/other/default.json")

    def __init__(self, name, save=False):
        self.name = name
        self.inventory = Inventory()  # Creates Inventory

        # Sets stats of character to save data. If save=false, uses default character data.
        characterData = self.readSave(name) if save else self.defaultSave
        self.statsFromJSON(characterData)

    def readSave(self, fileName):
        """Runs readFileJSON after defining the path with the fileName"""
        path = f"data/players/{fileName}.json"
        return saveFile.readFileJSON(path)

    def createSave(self):
        """Saves the character's data to a JSON file labeled under the characters name."""
        # DICT version of the characters information
        characterData = {
            "levels": self.levels,
            "levelPoints": self.levelPoints,
            "skills": self.skills,
            "inventory": self.inventory.toJSON(),
        }
        path = f"data/players/{self.name}.json"

        saveFile.saveFile(path, characterData)

    def statsFromJSON(self, JSON):
        """Sets the characters data to the corresponding values in the JSON input"""
        self.levels = JSON["levels"]
        self.levelPoints = JSON["levelPoints"]
        self.skills = JSON["skills"]

        self.inventory.itemsFromJSON(JSON["inventory"])

    def addItem(self, item, amount=1, level=1):
        """Adds an item to the players inventory"""
        self.inventory.addItem(item, amount, level)

    def getItems(self, display=[]):
        """Returns all of the Inventory. Pass ["item","display","amount","level", "equipped", "type", "rarity", "description",] to return item info"""

        return self.inventory.getItems(display)


bob = Character("temp", save=True)
print(bob.getItems(display=["description"]))
bob.addItem("bow-wood")
print(bob.getItems(display=["description"]))
