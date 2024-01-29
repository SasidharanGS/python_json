import store
import json
import os

class AddressBook():
    '''
    store and manage contact info
    '''
    def __str__(self):
        return "The only AddressBook you will ever need!"
    
    def print_info(self, dic, name=None):
        if name in dic:
            names_to_print = [name]
        else:
            if name is None:
                names_to_print = dic
            else:
                print("Person not found!")
                return_control()
        print("-"*50)
        for n in names_to_print:
            info = dic[n]
            print(f"\nName: {n}")
            print(f"\nPhone: {info['phone']}")
            print(f"\nEmail: {info['email']}")
            print(f"\nAddress: {info['address']}")
            print("-"*50)

    def add_contact(self):
        store.store_individual_data()
        return_control()

    def view_all_contacts(self):
        contacts = json_reader()
        if contacts is None:
            print("No contacts present!")
        else:
            self.print_info(contacts)
        return_control()
    
    def search_name(self):
        contacts = json_reader()
        inp = input("Enter contact name to search for:")
        self.print_info(contacts, inp)
        return_control()
    
    def update_name(self):
        contacts = json_reader()
        name = input("Enter contact name to update:")
        matches = [name] if name in contacts else False
        if matches:
            raw_data = store.convert_to_dictionary()
            corrected_data={}
            corrected_data[raw_data["name"]] = raw_data
            contacts.update(corrected_data)
            store.write_to_json(contacts)
        return_control()


def json_reader():
    with open("contacts.json", "r") as fp:
        try:
            c = json.load(fp)
        except:
            print("File empty or incorrect JSON format")
            c = {}
    return c

def starting_menu():
    os.system("cls")
    print("WELCOME TO ADRSBK".center(60))
    print("\n1. Add contacts")
    print("2. View all contacts")
    print("3. Search by name")
    print("4. Update by name\n")
    inp = input("Enter your action:")
    obj = AddressBook()
    validate_input(inp, obj)

def return_control():
    inp = input("\n"+"Continue using ADRSBK? (y/n)".rjust(45))
    if inp=="y" or inp=="Y":
        starting_menu()
    elif inp=="n" or inp=="N":
        os.system("cls")
        exit()
    else:
        print("Invalid input")
        return_control()

def validate_input(inp, obj):
    if inp=="1":
        obj.add_contact()
    elif inp=="2":
        obj.view_all_contacts()
    elif inp=="3":
        obj.search_name()
    elif inp=="4":
        obj.update_name()
    elif inp=="5":
        os.system("cls")
        exit()
    else:
        inp = input("Enter valid input (1/2/3/4)")
        validate_input(inp, obj)

starting_menu()