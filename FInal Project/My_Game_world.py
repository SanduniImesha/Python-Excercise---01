from Item import Item
from Room import Room


def create_world():
    """Create the rooms and items of the game.
    Returns a list of all rooms. The first room is the starting room."""
    entrance = Room(
        "Village Entrance",
        "An old gate stands open. You hear strange sounds.")
    village = Room(
        "Dark Village",
        "Ruined houses everywhere. It is very dark here. Something shines on the ground. "
        "A narrow path leads into the forest.",
        Item("Spell scroll", 0))
    cemetery = Room(
        "Old Cemetery",
        "Ghosts wander between the graves. A silver locket lies on a tombstone. "
        "Stone steps lead down to a crypt.",
        Item("Silver locket", 0.2))
    gate = Room(
        "Castle Gate",
        "A huge castle. An old guard stands in front of the door.")
    hall = Room(
        "Castle Hall",
        "A dark hall with cobwebs. A rusty key hangs on a hook by the wall. "
        "High up there is a broken window. "
        "At the end of the hall you see a gap and a heavy door.",
        Item("Old key", 0.3))
    secret = Room(
        "Secret Room",
        "A hidden room. In the middle there is an ancient chest.",
        Item("Ancient Gold Spell Stick", 1.5))

    # rooms for the other two routes
    forest = Room(
        "Forest Path",
        "A narrow path winds through old trees. Through the branches you can see the castle wall.")
    wall = Room(
        "Castle Wall",
        "You stand under the tall castle wall. High above you there is a broken window.")
    crypt = Room(
        "Crypt Tunnel",
        "A cold stone tunnel under the cemetery. Strange symbols cover the walls. "
        "At the end of the tunnel there is a small stone door.")

    # connect the rooms. Three different routes lead to the Secret Room:
    # Route 1 (guard route): village -> cemetery -> gate -> hall -> secret
    # Route 2 (wall route):  village -> forest -> wall -> hall -> secret
    # Route 3 (crypt route): village -> cemetery -> crypt -> secret

    
    entrance.connect(village)
    village.connect(cemetery)
    village.connect(forest)
    cemetery.connect(gate)
    cemetery.connect(crypt)
    forest.connect(wall)
    gate.connect(hall)
    wall.connect(hall)
    hall.connect(secret)
    crypt.connect(secret)

    return [entrance, village, cemetery, gate, hall, secret, forest, wall, crypt]


def create_start_items():
    """The items that the player has in the backpack at the start."""
    items = [Item("Torch", 0.5), Item("Rope", 1.5)]
    for i in range(3):
        items.append(Item("Gold coin", 0.1))
    return items