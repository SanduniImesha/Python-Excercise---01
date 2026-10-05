from Player import Player
from My_Game_world import Room, Item, create_start_items, create_world
from save import save_game, load_game, save_exists


def main():
    print("=== The Ancient Gold Spell Stick ===")
    age = int(input("Enter your age: "))

    if age < 12:
        print("You are a minor. The program will now close.")
        return
    else:
        name = input("What is your name? ")
    print(f"Welcome, {name}!")

# rooms where the player cannot see anything without a torch
DARK_ROOMS = ["Dark Village", "Castle Hall"]

def ask_age():
    """Ask the age until the user gives a number."""
    while True:
        try:
            return int(input("Enter your age: "))
        except ValueError:
            print("Please enter a number.")

def print_menu():
    print("\n--- Main Menu ---")
    print("kartta  - look at the map")
    print("katso   - look around")
    print("liiku   - move to another room")
    print("ota     - collect the item in this room")
    print("reppu   - show your backpack")
    print("taika   - cast a spell")
    print("bell    - ring the bell")
    print("tallenna - save the game")
    print("lopeta  - quit")

def too_dark(player):
    """True if the room is dark and the player has no torch."""
    return player.location.name in DARK_ROOMS and not player.has_item("Torch")

def show_map(player):
    print(f"You are here: {player.location.name}")
    print("You can go to:")
    for room in player.location.exits:
        print(f"  - {room.name}")

def look_around(player):
    room = player.location
    print(room.description)
    if too_dark(player):
        print("It is too dark. You need a torch to see anything.")
    elif room.item is not None:
        print(f"You see an item: {room.item.name}")

def show_backpack(player):
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

    return True

def move_player(player, state):
    destination = choose_destination(player)
    if destination is not None and can_enter(player, destination, state):
        player.move(destination)
        print(destination.description)

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
    age = ask_age()

    if age < 12:
        print("You are a minor. The program will now close.")
        return
    else:
        name = input("What is your name? ")
    print(f"Welcome, {name}!")
    print("You have an old map. It shows where the lost Ancient Gold Spell Stick is.")

    # create the objects: rooms, items and the player
    rooms = create_world()
    player = Player(name, rooms[0])
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
        elif command == "tallenna":
            save_game(player, state)
        elif command == "lopeta":
            print("Good Bye!")
            break
        else:
            print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
