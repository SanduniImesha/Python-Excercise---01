# The Ancient Gold Spell Stick

# TAGSS

## Storyline

The player is a young adventurer who gets an old mysterious map. The map shows where the ancient gold spell stick is hidden. The stick has been lost for many years.

The map leads to an abandoned village. Nobody lives there anymore. The village is dark and quiet, and it has an old cemetery, ruined buildings and a large ancient castle. Ghosts wander in the cemetery. An old guard stands at the castle gate. Somewhere inside the castle, in a secret room, lies an ancient chest.

The player starts with a backpack that has three important items ---->

### Item	Use

* In the Dark Village Room, you can collect a Spell Scroll. It helps protect you from the ghost.
* In the Cemetery, you can collect a Silver Locket. It helps you pass through the cemetery safely.
* In the Hall, you can collect an Old Key. It helps you open the door to the secret room.
* In the Secret Room, you can find an Ancient Gold Spell Stick.
* At the Castle Wall, you can use the Rope to get through the wall. The rope is already in your backpack.
* Your Backpack also has a Gold Coin. You can give the gold coin to the guard to leave through the castle gate.
* The Torch helps you see and move through dark places.

### Objective

Follow the map through the abandoned village, get past the cemetery and the castle, reach the Secret Room and collect the Ancient Gold Spell Stick.

The game is won when the stick is collected. The game also ends when the player types lopeta (quit).

The player has to make choices. There are three different routes to the Secret Room, and each one needs different items and different decisions.

### Route
   connect the rooms. Three different routes lead to the Secret Room:
     * Route 1 (guard route): village -> cemetery -> gate -> hall -> secret room
     * Route 2 (wall route):  village -> forest -> wall -> hall -> secret room
     * Route 3 (crypt route): village -> cemetery -> crypt -> secret room

### How to run the game

You need Python 3. No other libraries are needed.

At the start the game:

* shows the intro story (from Intro.txt),
* asks for the age (numbers only, it asks again if the answer is not a number). Players under 12 get a message and the program closes,
* asks for the name,
* if a saved game exists, asks if the player wants to load it.

## Commands

* kartta -	map	Shows the current room and the rooms you can go to
* katso -	look	Shows the description of the room and the item in it
* liiku -	move	Shows the exits as a numbered list. Type a number to move there, if the rules allow it
* takaisin - go back to the previous room
* ota -	take	Collects the item in the room
* reppu -	backpack	Shows the items in the backpack and their total weight
* taika -	spell	Casts the spell from the Spell scroll. It makes the ghosts go away
* bell -	bell	Rings the bell (only a message)
* ohje -	instructions	-Shows the instructions, which are read from instructions.txt
* tallenna -	save	- Saves the game to savegame.txt
* lopeta -	quit	- Ends the game



## Game rules

* If the age is under 12, the program ends.
* The village and the castle hall are dark. You need the torch to find items.
* The ghosts block the cemetery. Find the spell scroll in the village and use taika.
* The castle guard takes one gold coin when you enter the castle hall.
* The secret room needs the old key (from the cemetery) and the rope.
* The game is won when you collect the Ancient Gold Spell Stick.

## Operating Principles

* Start-up. main.py shows the intro, asks the age and the name, and creates the objects: the rooms (create_world), the player (at the first room) and the starting items (create_start_items). A dictionary called state remembers the story progress (ghosts_gone, guard_paid).

* Main loop. A while True loop prints the menu, reads one command and calls the right function. After every command the loop starts again. The loop ends with break when the player wins or types lopeta.

* Moving. liiku shows the exits of the current room. When the player chooses one, can enter checks the rules. It returns True or False and prints the reason if the player is stopped. Only if it returns True, the player is moved. can enter also looks at the room where the player is now, because the same room has different rules from different directions (for example the Castle Hall from the gate or from the wall).

* Collecting. Player.collect item moves the item from the room into the backpack. If the item is the Ancient Gold Spell Stick, the game is won.

* Objects. The Player knows its location ( Room ) and its items (a list of Item objects). A Room knows its item and its exits .

* Files. The game reads Intro.txt and instructions.txt.

* Wrong input. Letters as the age, a wrong menu number, an unknown command and a missing text file do not crash the game. The user gets a message instead.

## Project Structre

## ancient_gold_spell_stick

###  ├──README.md        (this file)
###  ├─main.py          (starts the game, menu loop and game)
###  ├── intro.txt      (story text shown when a new game) 
###  ├── instructions.txt   (how to play, shown at the start)
###  ├── item.py        (class Item)
###  ├── room.py        (class Room)
###  ├── player.py      (class Player)
###  ├── my_Game_world.py     (creates the rooms and the starting items)
###  └── save.py              (saves the game to a file and loads it back)



#### Item.py, Room.py, Player.py -	the classes of the game
#### My_Game_world.py	- the content of the game (rooms, items, story texts, connections)
#### save.py -	reading and writing the save file
#### Textfiles.py -	reading the intro text file
#### main.py	- the user interface and the rules

## Sustainable development perspective

The game takes into account the UN Sustainable Development Goal Sustainable cities and communities, especially target  about protecting and safeguarding the world's cultural heritage.

* The story is about an abandoned village and a lost old object. This is a small example of cultural heritage that is in danger of being forgotten.
* The objective. The player does not search for treasure to keep. The player searches for an object that belongs to the history of a community. At the end of the game the player carries the Ancient Gold Spell Stick back to the village, where it will be protected as part of the village's history, and the village "is not forgotten any more". 
* Peaceful solutions. The player does not fight. The ghosts are not harmed, they fade away when the spell is cast. The player solves problems with items, clues and choices, which also makes the game suitable for school-age playeer.

## Code quality and comments

* Every class and function has a docstring that tells what it does, what it gets and what it returns.
* Comments explain the parts that are not obvious, the rules of the three routes, the order of the exits, the save file format, and why some checks are written the way they are.
* Names are descriptive (can_enter, collect_item, ghosts_gone).
* Constants are written in capital letters (DARK_ROOMS, WINNING_ITEM).