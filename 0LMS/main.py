'''
LIBRARY MANAGEMENT SYSTEM
1. Display available books
2. Get book details
3. Borrow book
4. Return book
5. Add new book 
6. Exit 
'''


import pickle



BOOKS = []

def addBook():
    try:
        with open("library.dat", "rb") as f:
            BOOKS = pickle.load(f)
    except:
        BOOKS = []
    
    bookName = input("Enter book name: ")
    bookPub = input("Enter publisher name: ")
    bookAuth = input("Enter author name: ")
    bookGen = input("Enter genre: ")
    status = "available"

    BOOKS.append([bookName, bookPub, bookAuth, bookGen, status])

    with open("library.dat", "wb") as f:
        pickle.dump(BOOKS, f)
        print("Book added...")


def availBooks():
    try:
        with open("library.dat", "rb") as f:
            BOOKS = pickle.load(f)
    except:
        print("Library is empty!!")
    else:
        for book in BOOKS:
            if book[-1] == "borrowed":
                print(f"** {book[0]} ; Borrowed")
            elif book[-1] == "available":
                print(f"** {book[0]} ; Available")


def borrowBook():
    found = False
    try:
        with open("library.dat", "rb") as f:
            BOOKS = pickle.load(f)
    except:
        print("Library is empty!!")
    else:
        bookName = input("Enter book name: ")
        for index, book in enumerate(BOOKS[::]):
            if book[0] == bookName:
                found = True
                
                print(BOOKS[index][4])
                if book[4] != "borrowed":
                    print("borrowed a book")
                    BOOKS[index].pop()
                    BOOKS[index].append("borrowed")
                elif book[4] == "borrowed":
                    print("Book is already borrowed!!")

        if not found:
            print("Book not found!!")

        with open("library.dat", "wb") as f:
            pickle.dump(BOOKS, f)


def returnBook():





welcome = '''
LIBRARY MANAGEMENT SYSTEM
1. Display available books
2. Get book details
3. Borrow book
4. Return book
5. Add new book 
6. Exit
'''


def main():
    run = True
    while run:
        print(welcome)

        try:
            choice = int(input("Enter choice: "))
            if choice not in (1, 2, 3, 4, 5, 6):
                raise ValueError
        except ValueError:
            print("Invalid choice!!")
        else:
            if choice == 1:
                availBooks()
            elif choice == 2:
                pass
            elif choice == 3:
                borrowBook()
            elif choice == 4:
                returnBook()
            elif choice == 5:
                addBook()
            else:
                run = False





main()






