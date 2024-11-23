import json
import os

def readFileJSON(path):
    '''Returns the contents of a JSON file'''
    with open(path, 'r') as file:
        data = json.load(file)
    return data

def saveFile(path, JSON):
    '''Creates a save file based on a JSON input. Will overwrite files.'''
    if os.path.exists(path): os.remove(path) # Delete file with same path
    with open(path, 'w') as file: # Create and Opens new JSON file
        file.write(json.dumps(JSON)) # Write to the file the JSON input converted to a string
