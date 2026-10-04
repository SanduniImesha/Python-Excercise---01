import os

from Item import Item
from Player import Player

SAVE_FILE = "save.py"
def save_exists():
    """Return True if a save file has been made before."""
    return os.path.exists(SAVE_FILE)

def save_game(player, state):
    """Write the game progress to a text file (one value per line)."""
    with open(SAVE_FILE, "w") as file:
        file.write(player.name + "\n")                  # line 1: name
        file.write(player.location.name + "\n")         # line 2: room name
        file.write(str(state["ghosts_gone"]) + "\n")    # line 3: True or False
        file.write(str(state["guard_paid"]) + "\n")     # line 4: True or False
        for item in player.items:                       # line 5 onwards: items
            file.write(f"{item.name},{item.weight}\n")
    print("Game saved.")

def load_game(rooms):
    """Read the save file and return the player and the state."""
    with open(SAVE_FILE, "r") as file:
        lines = file.read().splitlines()

    name = lines[0]
    room_name = lines[1]
    state = {
        "ghosts_gone": lines[2] == "True",
        "guard_paid": lines[3] == "True",
    }

    # find the room where the player was
    location = rooms[0]
    for room in rooms:
        if room.name == room_name:
            location = room

    # make the player and fill the backpack from the file
    player = Player(name, location)
    for line in lines[4:]:
        item_name, weight = line.split(",")
        player.items.append(Item(item_name, float(weight)))

    # items that the player already has must not be in the rooms anymore
    for room in rooms:
        if room.item is not None and player.has_item(room.item.name):
            room.item = None

    return player, state
