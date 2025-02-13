from enum import Enum
from typing import OrderedDict
<<<<<<< HEAD
from pydantic import BaseModel

=======

from pydantic import BaseModel


>>>>>>> 9653950 (fresh git)
class Genre(str, Enum):
    """Book genres."""

    SCI_FI = "Science Fiction"
    FANTASY = "Fantasy"
    HORROR = "Horror"
    MYSTERY = "Mystery"
    ROMANCE = "Romance"
    THRILLER = "Thriller"

<<<<<<< HEAD
=======

>>>>>>> 9653950 (fresh git)
class Book(BaseModel):
    """Book schema

    Args:
        BaseModel (BaseModel): Pydantic base model.
    """
<<<<<<< HEAD
=======

>>>>>>> 9653950 (fresh git)
    id: int
    title: str
    author: str
    publication_year: int
    genre: Genre

<<<<<<< HEAD
=======

>>>>>>> 9653950 (fresh git)
class InMemoryDB:
    def __init__(self):
        self.books: OrderedDict[int, Book] = {}

    def get_books(self) -> OrderedDict[int, Book]:
        """Gets books from database.

        Returns:
            OrderedDict[int, Book]: Ordered dictionary of books.
        """
        return self.books
<<<<<<< HEAD
    
=======

>>>>>>> 9653950 (fresh git)
    def add_book(self, book: Book) -> Book:
        """Adds book to database.

        Args:
            book (Book): Book to add.

        Returns:
            Book: Added book.
        """
        self.books.update({book.id: book})

    def get_book(self, book_id: int) -> Book:
        """Gets a specific book from database.

        Args:
            book_id (int): Book ID.

        Returns:
            Book: Book.
        """
        return self.books.get(book_id)
    
    def update_book(self, book_id: int, data: Book) -> Book:
        """Updates a specific book in database.

        Args:
            book_id (int): Book ID.
            data (Book): Book data.

        Returns:
            Book: Updated book.
        """
        self.books.update({book_id: data})
        return self.books.get(book_id)

<<<<<<< HEAD
    def delete_book(self, book_id: int) -> None: 
=======
    def delete_book(self, book_id: int) -> None:
>>>>>>> 9653950 (fresh git)
        """Deletes a specific book from database.

        Args:
            book_id (int): Book ID.
        """
        if book_id in self.books:
            del self.books[book_id]
<<<<<<< HEAD
            
=======
>>>>>>> 9653950 (fresh git)
