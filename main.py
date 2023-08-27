from tape import Tape
from book import Book
from publication import Publication

def main() -> None:
    print("!main!")
    book = Book("title", 10.2, 154)
    tape = Tape("title", 10.2, 10.5)

    print("get book data: ")
    print(book.getdata())
    print("get tape data: ")
    print(tape.getdata())

    print("put book data: ")
    book.putdata("title", 10.2, 154)
    print("put tape data: ")
    tape.putdata("title", 10.2, 154)

if __name__ == "__main__":
    main()
