from Item import Item
from Room import Room

def create_world():
    """Create the rooms and items of the game.
    Returns a list of all rooms. The first room is the starting room."""
    entrance = Room(
        "Village Entrance",
        "An old gate stands open. you hear strange sounds.")
    village = Room(
        "Dark Village",
        "Ruined houses everywhere. It is very dark here. Something shines on the ground.",
        Item("Spell scroll", 0))
    cemetery = Room(
        "Old Cemetery",
        "Ghosts wander between the graves. A rusty key lies on a tombstone.",
        Item("Old key", 0.3))
    gate = Room(
        "Castle Gate",
        "A huge castle. An old guard stands in front of the door.")
    hall = Room(
        "Castle Hall",
        "A dark hall with cobwebs. At the end of the hall you see a gap and a heavy door.")
    secret = Room(
        "Secret Room",
        "A hidden room. In the middle there is an ancient chest.",
        Item("Ancient Gold Spell Stick", 1.5))

    # connect the rooms into a path
    entrance.connect(village)
    village.connect(cemetery)
    cemetery.connect(gate)
    gate.connect(hall)
    hall.connect(secret)

    return [entrance, village, cemetery, gate, hall, secret]

def create_start_items():
    """The items that the player has in the backpack at the start."""
    items = [Item("Torch", 0.5), Item("Rope", 1.5)]
    for i in range(3):
        items.append(Item("Gold coin", 0.1))
    return items
