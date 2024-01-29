import json

def convert_to_dictionary():
    inp1 = input("\nEnter your Name:\n")
    inp2 = int(input("\nEnter your Phone number:\n"))
    inp3 = input("\nEnter your Email:\n")
    address_lines = []
    print("\nEnter your Address:")
    while True:
        line = input()
        if line:
            address_lines.append(line)
        else:
            break
    address_text = '\n'.join(address_lines)
    dic = {
        "name":f"{inp1}",
        "phone":f"{inp2}",
        "email":f"{inp3}",
        "address":f"{address_text}"
    }
    return dic

def preprocess(d):
    with open("contacts.json", "r") as fp:
        try:
            existing_data = json.load(fp)
        except ValueError:
            existing_data = {}
    existing_data[d["name"]] = d
    return existing_data

def write_to_json(dic):
    with open("contacts.json", "w") as fp:
        json.dump(dic, fp)

def store_individual_data():
    dic = convert_to_dictionary()
    data = preprocess(dic)
    write_to_json(data)
    print("Record added to AddressBook!")