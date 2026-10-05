class Item:
    """An object that the player can carry in the backpack."""

    def __init__(self, name, weight):
        self.name = name        # ex: Torch
        self.weight = weight    # weight in kilograms

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"
