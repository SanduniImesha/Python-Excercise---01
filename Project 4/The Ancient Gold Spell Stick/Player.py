class Player:
    """The Player. Has a name, a list of items and a location."""

    def __init__(self, name, location):
        self.name = name
        self.items = []           # list of Item objects (the backpack)
        self.location = location  # the Room where the player is now

    def move(self, destination):
        """Move the player to another room."""
        self.location = destination
        print(f"You walk to: {destination.name}")

    def collect_item(self):
        """Take the item from the current room and put it in the backpack.
        Returns the item, or None if the room has no item."""
        room = self.location
        if room.item is None:
            print("There is nothing to collect here.")
            return None

        item = room.item
        self.items.append(item)
        room.item = None
        print(f"You collected: {item.name}")
        return item

    def has_item(self, name):
        """Check if the backpack contains an item with this name."""
        for item in self.items:
            if item.name == name:
                return True
        return False

    def remove_item(self, name):
        """Remove one item with this name. Returns True if it was found."""
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return True
        return False

    def total_weight(self):
        """Add together the weight of all items in the backpack."""
        total = 0
        for item in self.items:
            total += item.weight
        return round(total, 1)

