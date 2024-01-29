import store, helper
import os

class Library():
    '''
    store and manage library book info
    '''
    def __str__(self):
        return "library management class"
    def add_book(self):
        store.store_individual_data()
        return_control()
    def remove_book(self):
        pass
    def display_books(self):
        books = helper.json_reader()
        if books is None:
            print("No books found!")
        else:
            self.print_info(books)
        return_control()
    def search_title(self):
        books = helper.json_reader()
        inp = input("Enter Title to search for:")
        self.print_info(books, inp)
        return_control()
    def update_title(self):
        books = helper.json_reader()
        title = input("Enter Title name to update:")
        final_data = validate_title(title)
        books.update(final_data)
        helper.write_to_json(books)
        return_control()
    def print_info(self, dic, title=None):
        if title in dic:
            titles_to_print = [title]
        else:
            if title is None:
                titles_to_print = dic
            else:
                print("Person not found!")
                return_control()
        print("-"*50)
        for t in titles_to_print:
            info = dic[t]
            for key, value in info.items():
                print(key, ":", value)
            print("-"*50)
    
def validate_title(t):
    matches = [t] if t in t else False
    if matches:
        raw_data = store.convert_to_dictionary()
        corrected_data={}
        corrected_data[raw_data["title"]] = raw_data
        return corrected_data
    else:
        t = input("Enter a valid Title!")
        validate_title(t)

class Book(Library):
    def __str__(self):
        return "Base Book class"
    def __init__(self, t="Untitled", a="Anonymous", p="Unknown"):
        self.title = t
        self.author = a
        self.publication_year = p
    
class Ebook(Book):
    def __str__(self):
        return "Ebook class (extra=fileforamt)"
    def __init__(self, ff="Unspecified"):
        super().__init__()
        self.file_format = ff
    
class PaperBook(Book):
    def __str__(self):
        return "Paperbooks (extra=isbn, pages)"
    def __init__(self, isbn="Unspecified", pages=None):
        super().__init()
        self.isbn = isbn
        self.pages = pages

def return_control():
    inp = input("\n"+"Continue using LBRY? (y/n)".rjust(45))
    if inp=="y" or inp=="Y":
        starting_menu()
    elif inp=="n" or inp=="N":
        os.system("cls")
        exit()
    else:
        print("Invalid input")
        return_control()
    
def starting_menu():
    os.system("cls")
    print("WELCOME TO LBRY".center(60))
    print("\n1. Add book")
    print("2. View all books")
    print("3. Search by name")
    print("4. Update by name")
    print("5. Exit\n")
    inp = input("Enter your action:")
    validate_menu(inp)
    
def validate_menu(i):
    lib = Library()
    if i=="1":
        #add book
        lib.add_book()
    elif i=="2":
        #view books
        lib.display_books()
    elif i=="3":
        #search
        lib.search_title()
    elif i=="4":
        #update
        lib.update_title()
    elif i=="5":
        os.system("cls")
        exit()
    else:
        i = input("Enter valid input!")
        validate_menu(i)

starting_menu()