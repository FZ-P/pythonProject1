# Ex11_1.py

class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_details(self):
        print(f"Book Title: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, editor_in_chief):
        super().__init__(name)
        self.editor_in_chief = editor_in_chief

    def print_details(self):
        print(f"Magazine Title: {self.name}")
        print(f"Editor-in-Chief: {self.editor_in_chief}")


# Main program to test the publication hierarchy
if __name__ == "__main__":
    magazine = Magazine("Aku Ankka", "Aki Hyyppä")
    book = Book("Hytti n:o 6", "Rosa Liksom", 200)

    # Print details of each publication
    magazine.print_details()
    print()  # Empty line for separation
    book.print_details()
