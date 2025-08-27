library = ["python for beginners", "data structures in c", "basics"]
borrowed_book = {}
def start():
    while True:
        print("""
        1. display all books
        2. add books
        3. borrow book
        4. return book
        5. show borrowed books
        6. students that borrowed books
        7. exit
        """)
        user_choice = input(">>>>>")
        call_function(user_choice)
def call_function(user_choice):
    if user_choice == "1":
        display_books()
    elif user_choice == "2":
        book_name = input("book to add\n>>")
        add_book(book_name)
    elif user_choice == "3":
        book_name = input("book to borrow: ")
        borrow_book(book_name)
    elif user_choice == "4":
        book_name = input("name of book to return")
        return_book(book_name)
    elif user_choice == "5":
        show_borrowed_books()
 #   elif user_choice == "6":
  #      students_that_borrowed_books()
def display_books():
    if len(library) != 0:
        for book in library:
            print(book)
    else:
        print("no books in the libraby")
def add_book(book_name):
    if book_name in library:
        print("book already exist")
    else:
        library.append(book_name)
        print(f"{book_name} successfully added")
def borrow_book(book_name):
    #global student_id
    if book_name in library:
        library.remove(book_name)
        borrowed_book[book_name] = True
        #borrowed_book[student_id] = book_name
        #student_id += 1
        print(f"you borrowed {book_name}")
    else:
        print("not available")
def return_book(book_name):
    if book_name in borrowed_book:
        del borrowed_book[book_name]
        library.append(book_name)
        print(f"book {book_name} return successfully")
    else:
        print("book not borrowd in library")
def show_borrowed_books():
    if len(borrowed_book) > 0:
        print("borrowed books")
        for book_name in borrowed_book:
            print("_", book_name)
    else:
        print("no borrowed books")
#def students_that_borrowed_book():
        
start()
