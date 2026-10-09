import os
from Player import Player
from My_Game_world import Room, Item, create_start_items, create_world
from save import save_game, load_game, save_exists
import Textfiles 


def main():
    print("=== The Ancient Gold Spell Stick ===")


    age = int(input("Enter your age: "))

    if age < 12:
        print("You are a minor. The program will now close.")
        return
    else:
        name = input("What is your name? ")
    print(f"Welcome, {name}!")


def read_text_file(filename: str) -> str:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Instructions file not found."


Textfiles.show_Intro()


# rooms where the player cannot see anything without a torch
DARK_ROOMS = ["Dark Village", "Castle Hall"]


def print_menu():
    print("\n--- Main Menu ---")
    print("kartta  - look at the map")
    print("katso   - look around")
    print("liiku   - move to another room")
    print("takaisin - go back to the previous room")
    print("ota     - collect the item in this room")
    print("reppu   - show your backpack")
    print("taika   - cast a spell")
    print("bell    - ring the bell")
    print("ohje    - show the instructions")
    print("tallenna - save the game")
    print("lopeta  - quit")

def too_dark(player):
    """True if the room is dark and the player has no torch."""
    return player.location.name in DARK_ROOMS and not player.has_item("Torch")

def show_map(player):
    """Show where the player is and which rooms are next to it."""
    print(f"You are here: {player.location.name}")
    print("You can go to:")
    for room in player.location.exits:
        print(f"  - {room.name}")

def look_around(player):
    """Describe the room and show the item if the player can see it."""
    room = player.location
    room = player.location
    print(room.description)
    if too_dark(player):
        print("It is too dark. You need a torch to see anything.")
    elif room.item is not None:
        print(f"You see an item: {room.item.name}")

def show_backpack(player):
    """Show the items in the backpack and their total weight."""
    print("Your backpack contains:")
    for number, item in enumerate(player.items, start=1):
        print(f"  {number}. {item}")
    print(f"Total weight: {player.total_weight()} kg")

def choose_destination(player):
    """Show the exits as a numbered list and let the user choose one."""
    exits = player.location.exits
    print("Where do you want to go?")
    for number, room in enumerate(exits, start=1):
        print(f"  {number}. {room.name}")

    choice = input("Choose a number: ")
    if choice.isdigit() and 1 <= int(choice) <= len(exits):
        return exits[int(choice) - 1]
    print("Invalid choice.")
    return None

def can_enter(player, room, state):
    """Check the rules of the story. Returns True if the player may enter."""
    if room.name == "Old Cemetery":
        if not player.has_item("Torch"):
            print("It is too dark to find the path. You need a torch.")
            return False
        if not state["ghosts_gone"]:
            print("The ghosts block your way! You need a spell (taika).")
            return False

    if room.name == "Castle Hall" and not state["guard_paid"]:
        if player.remove_item("Gold coin"):
            state["guard_paid"] = True
            print("The guard takes one gold coin and opens the door.")
        else:
            print("The guard wants one gold coin. You have none.")
            return False
        

    if room.name == "Secret Room":
        if not (player.has_item("Old key") and player.has_item("Rope")):
            print("The heavy door is locked and there is a gap in front of it.")
            print("You need the old key and a rope.")
            return False
  # Route 2 (wall route): the broken window is high, a rope is needed
    class where:
        ...

    if room.name == "Castle Hall" and where == "Castle Wall":
        if not player.has_item("Rope"):
            print("The broken window is high above you. You need a rope to climb up.")
            return False
        print("You throw the rope up and climb through the broken window.")
 
    # Route 3 (crypt route): the tunnel is dark
    if room.name == "Crypt Tunnel" and not player.has_item("Torch"):
        print("The stone steps lead down into complete darkness. You need a torch.")
        return False
 
    # The Secret Room has two doors
    if room.name == "Secret Room":
        if where == "Castle Hall":
            # the heavy door from the hall: old key and rope
            if not (player.has_item("Old key") and player.has_item("Rope")):
                print("The heavy door is locked and there is a gap in front of it.")
                print("You need the old key and a rope.")
                return False
        elif where == "Crypt Tunnel":
            # the small stone door from the crypt: silver locket
            if player.has_item("Silver locket"):
                print("You place the silver locket into the hollow. The stone door slides open!")
                return True  # Directly allows entry into the Secret Room
            else:
                print("The small stone door has a hollow in the shape of a locket.")
                print("You need the silver locket from the cemetery.")
                return False  # Blocks entry if they don't have it

    return True


def move_player(player, state):
    """Ask where to go and move the player if the rules allow it."""
    destination = choose_destination(player)
    if destination is not None and can_enter(player, destination, state):
        if not hasattr(player, "previous_room"):
            player.previous_room = None
        player.previous_room = player.location
        player.move(destination)
        print(destination.description)


def go_back(player):
    """Return to the previous room if one exists."""
    if not hasattr(player, "previous_room") or player.previous_room is None:
        print("You have nowhere to go back to.")
        return

    current_room = player.location
    previous_room = player.previous_room
    player.location = previous_room
    player.previous_room = current_room
    print(f"You go back to {player.location.name}.")
    print(player.location.description)


def collect(player):
    """Collect the item in the room. Returns the item or None."""
    if too_dark(player):
        print("It is too dark. You need a torch to find anything.")
        return None
    return player.collect_item()

def cast_spell(player, state):
    if not player.has_item("Spell scroll"):
        print("You do not know any spell yet. Find the spell scroll first.")
    elif state["ghosts_gone"]:
        print("Sparks fly from your fingertips, but the ghosts are already gone.")
    else:
        state["ghosts_gone"] = True
        print("You read the scroll and cast a spell! The ghosts fade into the fog.")

def main():
    print("=== The Ancient Gold Spell Stick ===")
    age = int(input("Enter your age: "))

    if age < 12:
        print("You are a minor. The program will now close.")
        return
    else:
        name = input("What is your name? ")
    print(f"Welcome, {name}!")
    print("You have an old map. It shows where the lost Ancient Gold Spell Stick is.")

    # create the objects: rooms, items and the player
    rooms = create_world()
    start_room = rooms[0]  # the first room in the list is the starting room
    player = Player(name, age, start_room)
    player.items = create_start_items()

    # things that change during the story
    state = {"ghosts_gone": False, "guard_paid": False}

    # if a save file exists, the user can continue the old game
    if save_exists():
        answer = input("A saved game was found. Load it? (yes/no): ").lower()
        if answer == "yes":
            player, state = load_game(rooms)
            print(f"Welcome back, {player.name}! You are in: {player.location.name}")

    while True:
        print_menu()
        command = input("> ").lower()

        if command == "kartta":
            show_map(player)
        elif command == "katso":
            look_around(player)
        elif command == "liiku":
            move_player(player, state)
        elif command == "takaisin":
            go_back(player)    
        elif command == "ota":
            item = collect(player)
            if item is not None and item.name == "Ancient Gold Spell Stick":
                print("\nYou open the chest and find the Ancient Gold Spell Stick!")
                print("You completed the quest. Congratulations!")
                break
        elif command == "reppu":
            show_backpack(player)
        elif command == "taika":
            cast_spell(player, state)
        elif command == "bell":
            print("You ring the bell. The sound echoes through the village.")
        elif command == "ohje":
            print(read_text_file("instructions.txt"))
        elif command == "tallenna":
            save_game(player, state)
        elif command == "lopeta":
            print("Good Bye!")
            break
        else:
            print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()