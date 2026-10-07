# The Ancient Gold Spell Stick

# TAGSS

## Storyline
The player is a young adventurer order than 12 with an old map. The map leads to an abandoned, spooky village, a cemetery full of ghosts and a large ancient castle. Somewhere in the castle is the lost Ancient Gold Spell Stick. The player starts with a backpack that has a torch, a rope and three gold coins.

### Items
* In the Dark Village Room, you can collect a Spell Scroll. It helps protect you from the ghost.
* In the Cemetery, you can collect a Silver Locket. It helps you pass through the cemetery safely.
* In the Hall, you can collect an Old Key. It helps you open the door to the secret room.
* In the Secret Room, you can find an Ancient Gold Spell Stick.
* At the Castle Wall, you can use the Rope to get through the wall. The rope is already in your backpack.
* Your Backpack also has a Gold Coin. You can give the gold coin to the guard to leave through the castle gate.
* The Torch helps you see and move through dark places.

### Route
   connect the rooms. Three different routes lead to the Secret Room:
     Route 1 (guard route): village -> cemetery -> gate -> hall -> secret
     Route 2 (wall route):  village -> forest -> wall -> hall -> secret
     Route 3 (crypt route): village -> cemetery -> crypt -> secret

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
###  ├── intro.txt      (story text shown when a new game) 
###  ├── instructions.txt   (how to play, shown at the start)
###  ├── item.py        (class Item)
###  ├── room.py        (class Room)
###  ├── player.py      (class Player)
###  ├── my_Game_world.py     (creates the rooms and the starting items)
###  └── save.py              (saves the game to a file and loads it back)

### File handling

The command "tallenna" writes the name, the room, the story progress and the backpack items to savegame.txt. When the game starts and a save file exists, the user can choose to load it and continue.
