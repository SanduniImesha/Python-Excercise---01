import os


BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_FOLDER, "Intro.txt")

with open(path, "r", encoding="utf-8") as file:
    text = file.read()


def show_Intro():
    print(text)