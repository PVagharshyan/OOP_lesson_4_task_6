from tape import Tape
from book import Book
from publication import Publication

def main() -> None:
    print("!main!")
    book = Book()
    tape = Tape()

    print("get book data: ")
    print(book.getdata())
    print("get tape data: ")
    print(tape.getdata())

    print("put book data: ")
    book.putdata()
    print("put tape data: ")
    tape.putdata()

if __name__ == "__main__":
    main()
