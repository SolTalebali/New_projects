print()
class Book:
  def __init__ (self, title, author):
    self.title = title
    self.author = author
    self.available = True

  def checkout(self):
    if self.available:
      self.available = False
      return True
    else:
      return False
    
  def return_book(self):
    self.available = True

  def display_info(self):
    print(f"Title: {self.title}\nAuthor: {self.author}")


book1 = Book("12 Rules for Life", "Jordan Peterson")
book2 = Book("Daisy Darker", "Alice Freeney")
book3 = Book("Zen and the Art of Motorcycle Maintenance", "Robert M. Pirsig")


class Library:
  def __init__ (self):
    self.books = []

  def add_book (self, book):
    self.books.append(book)

  def display_books(self):
    book_index = 1
    for book in self.books:
      print(f"Book {book_index}")
      book.display_info()
      print()
      book_index += 1
  
  def get_book_by_title(self, title):
    for book in self.books:
      if book.title == title:
        return book
      else:
        return None

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.display_books()