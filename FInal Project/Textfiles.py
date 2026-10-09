import os
 
# text files are in the same folder as this program
BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
INTRO_FILE = os.path.join(BASE_FOLDER, "Intro.txt")
 
def read_file(filename):
    """Return the content of a text file, or a message if it is missing."""
    path = os.path.join(BASE_FOLDER, filename)
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"({filename} not found)"


def show_Intro():
    """Print the story intro at the start of the game."""
    print(read_file("intro.txt"))


def handle_command(command):
    """Display instructions when the requested command matches 'ohje'."""
    if command == "ohje":
        print(read_file("instructions.txt"))