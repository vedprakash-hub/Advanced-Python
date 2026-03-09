# LIBRARY MANAGEMENT

lib = ["Python", "Java", "DBMS", "C++"]
issue = []

def display_book():
    print("\n Books Available: ")
    for a in lib:
        print(a)
    print("\n Books Issued: ")
    for b in issue:
        print(b)


def add_book():
    book = input("Enter name of book to add: ")
    lib.append(book)
    print("Book ",book," added")

def issue_book():
    book = input("Enter issued book name: ")
    if book in lib:
        lib.remove(book)
        issue.append(book)
        print("Book ",book," has been issued")
    else:
        print("Book not available in Library")

def return_book():
    book = input("Enter returning book name: ")
    if book in issue:
        issue.remove(book)
        lib.append(book)
        print("Book ",book," has been returned")
    else:
        print("The book has not been issued")

while True:
    print("\n 1.Display  2.Add  3.Issue  4.Return  5.Exit")
    ch = input("Enter your choice: ")

    if ch == "1":
        display_book()
    elif ch == "2":
        add_book()
    elif ch == "3":
        issue_book()
    elif ch == "4":
        return_book()
    elif ch == "5":
      print("Thank you Visiting our Library. Your total cost is $100")
      break
    else:
        print("There's only 5 options where did you get this number.")