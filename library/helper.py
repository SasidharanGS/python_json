import json

file_name = "books.json"

def json_reader():
    with open("books.json", "r") as fp:
        try:
            c = json.load(fp)
        except:
            print("File empty or incorrect JSON format")
            c = {}
    return c

def write_to_json(dic):
    with open(f"{file_name}", "w") as fp:
        json.dump(dic, fp)

def preprocess(d):
    with open(f"{file_name}", "r") as fp:
        try:
            existing_data = json.load(fp)
        except ValueError:
            existing_data = {}
    existing_data[d["title"]] = d
    return existing_data