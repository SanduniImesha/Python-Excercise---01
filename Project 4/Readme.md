# The Ancient Gold Spell Stick

# TAGSS

## Storyline
The player is a young adventurer order than 12 with an old map. The map leads to an abandoned, spooky village, a cemetery full of ghosts and a large ancient castle. Somewhere in the castle is the lost Ancient Gold Spell Stick. The player starts with a backpack that has a torch, a rope and three gold coins.

### Route
 Village Entrance - Dark Village - Old Cemetery - Castle Gate - Castle Hall - Secret Room

### Game rules

 If the age is under 12, the program ends.
 The village and the castle hall are dark. You need the torch to find items.
 The ghosts block the cemetery. Find the spell scroll in the village and use taika.
 The castle guard takes one gold coin when you enter the castle hall.
 The secret room needs the old key (from the cemetery) and the rope.
 The game is won when you collect the Ancient Gold Spell Stick.

# Project Structre

## ancient_gold_spell_stick/
### ├──README.md        (this file)
###  ├─main.py          (starts the game, menu loop and game)
###  ├── item.py        (class Item)
###  ├── room.py        (class Room)
###  ├── player.py      (class Player)
###  ├── my_Game_world.py     (creates the rooms and the starting items)
###  └── save.py              (saves the game to a file and loads it back)

###File handling

The command "tallenna" writes the name, the room, the story progress and the backpack items to savegame.txt. When the game starts and a save file exists, the user can choose to load it and continue.
