import json
import helper

def convert_to_dictionary():
    inp1 = input("\nEnter Book Title:\n")
    inp2 = input("\nEnter Author Name:\n")
    inp3 = input("\nEnter Publication Year:\n")
    extra_details = select_book_type()
    if len(extra_details)==1:   #ebook
        inp4 = extra_details[0]
        dic = {
            "title":f"{inp1}",
            "author":f"{inp2}",
            "publication_year":f"{inp3}",
            "file_format":f"{inp4}"
            }
    elif len(extra_details)==2: #paperbook
        inp4 = extra_details[0]
        inp5 = extra_details[1]
        dic = {
            "title":f"{inp1}",
            "author":f"{inp2}",
            "publication_year":f"{inp3}",
            "isbn":f"{inp4}",
            "pages":f"{inp5}"
            }
    return dic

def select_book_type():
    inp = input("Enter book type:\t1.EBook 2.PaperBook")
    extra_details = validate_addition(inp)
    return extra_details

def validate_addition(inp):
    if inp=="1":
        ff = input("Enter file format")
        return [ff]
    elif inp=="2":
        isbn = input("\nEnter isbn number:")
        pages = input("Enter number of pages:")
        return [isbn, pages]
    else:
        inp = input("Enter valid input!")
        validate_addition(inp)

def store_individual_data():
    dic = convert_to_dictionary()
    data = helper.preprocess(dic)
    helper.write_to_json(data)
    print("Record added to Library!")
