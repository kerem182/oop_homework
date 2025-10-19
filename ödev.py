from abc import ABC, abstractmethod

class LibraryItem(ABC):
    total_items = 0  

    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.__item_id = item_id   
        self._is_borrowed = False  
        LibraryItem.total_items += 1

    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

    @abstractmethod
    def info(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, LibraryItem):
            return NotImplemented
        return self.__item_id == other.__item_id

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.title}>"


class Book(LibraryItem):
    def __init__(self, title, author, pages, item_id):
        super().__init__(title, author, item_id)
        self.pages = pages

    def borrow(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            return f"Book '{self.title}' borrowed."
        return f"Book '{self.title}' already borrowed."

    def return_item(self):
        if self._is_borrowed:
            self._is_borrowed = False
            return f"Book '{self.title}' returned."
        return f"Book '{self.title}' was not borrowed."

    def info(self):
        return f"[Book] {self.title} by {self.author}, {self.pages} pages."


class Magazine(LibraryItem):
    def __init__(self, title, author, issue, item_id):
        super().__init__(title, author, item_id)
        self.issue = issue

    def borrow(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            return f"Magazine '{self.title}' Issue {self.issue} borrowed."
        return f"Magazine '{self.title}' already borrowed."

    def return_item(self):
        if self._is_borrowed:
            self._is_borrowed = False
            return f"Magazine '{self.title}' Issue {self.issue} returned."
        return f"Magazine '{self.title}' was not borrowed."

    def info(self):
        return f"[Magazine] {self.title}, Issue {self.issue}."


class EBook(LibraryItem):
    def __init__(self, title, author, file_size, item_id):
        super().__init__(title, author, item_id)
        self.file_size = file_size  

    def borrow(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            return f"EBook '{self.title}' has been downloaded."
        return f"EBook '{self.title}' is already borrowed."

    def return_item(self):
        if self._is_borrowed:
            self._is_borrowed = False
            return f"EBook '{self.title}' license released."
        return f"EBook '{self.title}' was not borrowed."

    def info(self):
        return f"[EBook] {self.title} by {self.author}, File size: {self.file_size} MB."


class Librarian:
    def __init__(self, name):
        self.name = name

    def lend_item(self, item: LibraryItem):
        print(f"{self.name} lends out {item.title}.")
        return item.borrow()

    def receive_item(self, item: LibraryItem):
        print(f"{self.name} receives {item.title}.")
        return item.return_item()


class Library:
    def __init__(self):
        self.items = []  
        self.librarian = None  
        self.report = LibraryReport(self)  

    def assign_librarian(self, librarian: Librarian):
        self.librarian = librarian
        print(f"Librarian {librarian.name} assigned to library.")

    def add_item(self, item):
        """Overloading-like behavior (different item types)"""
        if isinstance(item, Book):
            print(f"Added Book: {item.title}")
        elif isinstance(item, Magazine):
            print(f"Added Magazine: {item.title}")
        elif isinstance(item, EBook):
            print(f"Added EBook: {item.title}")
        else:
            print(f"Unsupported item type: {type(item)}")
            return
        self.items.append(item)

    def show_all(self):
        print("\nLibrary Collection:")
        for i in self.items:
            print("  -", i.info())

    def show_report(self):
        print("\n--- Library Report ---")
        print(self.report.generate_report())


class LibraryReport:
    def __init__(self, library):
        self.library = library 

    def generate_report(self):
        total = len(self.library.items)
        borrowed = sum(1 for i in self.library.items if i._is_borrowed)
        return f"Total: {total}, Borrowed: {borrowed}, Available: {total - borrowed}"

class Notifier:
    def notify(self, *messages, prefix="[INFO]"):
        """Simulates method overloading using variable args and default values."""
        for msg in messages:
            print(f"{prefix} {msg}")

if __name__ == "__main__":

    book = Book("1984", "George Orwell", 328, 1)
    magazine = Magazine("National Geographic", "Various", "Sep 2025", 2)
    ebook = EBook("Python Programming", "John Doe", 5, 3)

    library = Library()
    library.add_item(book)
    library.add_item(magazine)
    library.add_item(ebook)
    library.show_all()

    librarian = Librarian("Kerem Salih Erol")
    library.assign_librarian(librarian)

    print("\nBorrow/Return transactions:")
    print(librarian.lend_item(book))
    print(librarian.receive_item(book))
    print(librarian.lend_item(ebook))
    print(librarian.receive_item(ebook))

    another_book = Book("1984 Copy", "Unknown", 200, 1)
    print("\n--- Operator Overloading Test (==) ---")
    result = "SAME " if book == another_book else "NOT SAME"
    print(f"{book.title}  ↔  {another_book.title}  -->  {result}")

    library.show_report()

    print("\n--- Method Overloading Demo ---")
    notifier = Notifier()
    notifier.notify("Library updated", "3 new items added")
    notifier.notify("System maintenance scheduled!", prefix="[WARNING]")
