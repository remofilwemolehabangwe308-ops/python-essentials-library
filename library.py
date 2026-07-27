# Library Management Sytem - Remofilwe Molehanagwe - Python Essentials 1 

# Returns (total_copies, copies_available) across the whole library as a tuple 
def library_totals(books):
  pass
# Returns the book ID of the most-borrowed book, or None of no books
def most_borrowed(books):
  pass
# Asks for a number of copies, validates with try-except, returns int or None 
def read_valid_copies():
  pass
# Adds a new book OR adds copies to an existing titile by the same author
def add_book(books):
  pass
# Register a new member with an empty borrowed list
def register_member(members):
  pass
# One member borrows one book - enforces ALL the rules, updates BOTH dicts
def borrow_books(books, members):
  pass
# One member returns one bok - updates BOTH dicts
def return_book(books, members):
  pass
# Case-insensitive keywords search over titles
def search_catalogue(books):
  pass
# Prints one member with the TITLES of their borrowed books
def members_summary(books, members):
  pass
# Prints the whole-library report
def library_report(books, members):
  pass
# ----main program----
books = {}
members = {}
next_book_number = 1
next_member_number = 1
while True:
  print("1.Add a book\n2.Register a member\n3.Borrow a book\n4.Return a book\n5.Search the catalogue\n6.Member summary\n7.Library report\n8.Exit")
  choice = input("Enter your choice: ")
  if choice == "1":
    add_book(books) 
  elif choice == "2":
    register_member(members)
  elif choice == "3":
    borrow_books(books, members)
  elif choice == "4":
    return_book(books, members)
  elif choice == "5":
    search_catalogue(books)
  elif choice == "6":
    members_summary(books, members)
  elif choice == "7":
    library_report(books, members)
  elif choice == "8":
    print("Goodbye")
    break
  else:
    print("Invalid choice. Please try again.")
  
  
