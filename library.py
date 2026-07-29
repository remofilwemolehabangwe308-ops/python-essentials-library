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
  global next_book_number 

  title = input("Enter the book title: ")
  author = input("Enter the author of the book: ")
  number_of_copies = read_valid_copies()

  if not title:
    print("The tittle cannot be empty")
    return
  if not author:
    print("The author cannot be empty")
    return
  
  # Check for duplicates books
  for book_id in books:
    book_info = books[book_id]
    if book_info['title'].lower() == title.lower() and book_info['author'].lower() == author.lower():
      print("The book already exist, do not create the duplicate")
      total_copies = book_info['total_copies']
      total_copies += number_of_copies
      book_info['total_copies'] = total_copies
      available_copies = book_info['available_copies']
      available_copies += number_of_copies
      book_info['available_copies'] = available_copies 
      print(f'Added {number_of_copies} more copies of {book_id}:{title} now has {available_copies} total copies')

  # No duplicates found, create a new book
  book_id = "B" + str(next_book_number)
  next_book_number += 1
  total_copies = number_of_copies
  available_copies = number_of_copies
  books[book_id] = {
    "title": title,
    "author": author,
    "total_copies": total_copies,
    "available_copies": available_copies,
    "times_borrowed": 0 
   }
  print(f'Added {number_of_copies} copies of {title} by {author}')

def read_valid_copies():
  while True:
    try:
     number_of_copies = int(input("Enter the number of copies: "))
     if number_of_copies <= 0:
       print('That is not a valid number of copies.Please try again')
     else:
       return number_of_copies
    except ValueError:
      print("That is not a valid number of copies")

# Register a new member with an empty borrowed list
def register_member(members):
  global next_member_number
  member_name = input("Enter the name of the member: ")
  if not member_name:
    print("The member is blank, Rejected!!")
    return
  for member_id in members:
    if member_id in members:
      print(f'Member {member_id} already exist')
      return
  member_id = "M" + str(next_member_number)
  members[member_id] = {
    "name" : member_name,
    "borrowed_books" : []
  }
  next_member_number += 1
  print(f'Registered {member_id}; {member_name}')

  
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
  
  
