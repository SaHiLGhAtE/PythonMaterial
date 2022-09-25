# Library Management System

class Library:
    def __init__(self,list_of_books,library_name):
        # creating a dictionary of all books keys
        self.lend_data={}
        self.list_of_books=list_of_books
        self.library_name=library_name

        # adding books to dictionary
        for books in self.list_of_books:
            # none means nobody lends this book
            self.lend_data[books]=None

    def display_books(self):
        for index,books in enumerate(self.list_of_books):
            print(f"{index}:{books}")

    def lend_book(self,book,reader):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book]=reader
                print("Book Lend")
            else:
                print(f"Sorry this book is lend by {self.lend_data[book]}")
        else:
            print("You have written wrong book name")

    def return_book(self,book,reader):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("Sorry but this book is not lend")
        else:
            print("You have written a wrong book name")

    def add_book(self,book_name,reader):
        self.list_of_books.append(book_name)
        self.lend_data[book_name]=None

    def delete_book(self,book_name,reader):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)

def main():
    #By default variables
    list_books=["Cookbook","Sherlock Holmes","Chacha Chaudhary","Rich Dad and Poor Dad"]
    library_name="Sahil"
    secret_key=123

    Sahil=Library(list_books,library_name)

    print(f"Welcome To {Sahil.library_name} library\n\nq for exit \nDisplay Books Using 'd' and Lend a Book Using 'l' and Return a Book using 'r' \nAdd a Book Using 'a' and Delete a Book Using 'del' \n")
    Exit=False
    while(Exit is not True):
        _input=input("option:")
        print("\n")

        if _input=="q":
            Exit=True

        elif _input=="d":
            Sahil.display_books()

        elif _input=="l":
            _input2=input("What is your name")
            _input3=input("Which book do you want to lend")
            Sahil.lend_book(_input3,_input2)

        elif _input=="a":
            _input2=input("What is your name")
            _input3=input("Book name which you want to add")
            Sahil.add_book(_input3,_input2)

        elif _input=="del":
            _input_secret=int(input("Write the secret code to delete"))
            if _input_secret==secret_key:
                _input2=input("What is your name")
                _input3=input("Book which you want to delete")
                Sahil.delete_book(_input3,_input2)
            else:
                print("Sorry we can't delete this book")

        elif _input=="r":
            _input2=input("What is your name")
            _input3=input("Which book do you want to return")
            Sahil.return_book(_input3,_input2)


if __name__=='__main__':
    main()

