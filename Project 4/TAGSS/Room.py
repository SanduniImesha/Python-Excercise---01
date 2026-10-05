class Room:
    """A place in the game world. A room can contain one item."""

    def __init__(self, name, description, item=None):
        self.name = name
        self.description = description
        self.item = item      # one Item object, or None if the room is empty
        self.exits = []       # list of rooms that are connected to this room

    def connect(self, other_room):
        """Make a two-way path between this room and another room."""
        self.exits.append(other_room)
        other_room.exits.append(self)

    def __str__(self):
        return self.name
