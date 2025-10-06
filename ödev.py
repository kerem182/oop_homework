from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.__item_id = item_id
        self._is_borrowed = False

    def get_item_id(self):
        return self.__item_id

    def set_item_id(self, new_id):
        if new_id > 0:
            self.__item_id = new_id
        else:
            raise ValueError("Item ID must be positive")

    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

    @abstractmethod
    def info(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, author, pages, item_id):
        super().__init__(title, author, item_id)
        self.pages = pages

    def borrow(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            return f"Book '{self.title}' has been borrowed."
        else:
            return f"Book '{self.title}' is already borrowed."

    def return_item(self):
        if self._is_borrowed:
            self._is_borrowed = False
            return f"Book '{self.title}' has been returned."
        else:
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
        else:
            return f"Magazine '{self.title}' is already borrowed."

    def return_item(self):
        if self._is_borrowed:
            self._is_borrowed = False
            return f"Magazine '{self.title}' Issue {self.issue} returned."
        else:
            return f"Magazine '{self.title}' was not borrowed."

    def info(self):
        return f"[Magazine] {self.title} by {self.author}, Issue {self.issue}."

class EBook(LibraryItem):
    def __init__(self, title, author, file_size, item_id):
        super().__init__(title, author, item_id)
        self.file_size = file_size  

    def borrow(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            return f"EBook '{self.title}' has been downloaded."
        else:
            return f"EBook '{self.title}' is already borrowed."

    def return_item(self):
        if self._is_borrowed:
            self._is_borrowed = False
            return f"EBook '{self.title}' license has been released."
        else:
            return f"EBook '{self.title}' was not borrowed."

    def info(self):
        return f"[EBook] {self.title} by {self.author}, File size: {self.file_size} MB."

items = [
    Book("1984", "George Orwell", 328, 1),
    Magazine("National Geographic", "Various", "September 2025", 2),
    EBook("Python Programming", "John Doe", 5, 3)
]

for item in items:
    print(item.info())
    print(item.borrow())
    print(item.return_item())

    print("---")
