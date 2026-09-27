class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, pages):
        # call the base class initializer to set the shared "name" property
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(f"{self.name}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"{self.name}")
        print(f"Chief editor: {self.chief_editor}")


def main():
    donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
    compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)

    donald_duck.print_information()
    print()
    compartment_no_6.print_information()


if __name__ == "__main__":
    main()