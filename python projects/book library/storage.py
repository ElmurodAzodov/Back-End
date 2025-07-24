import json

def load_books():
    try:
        with open("books.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def save_books(data):
    with open("books.json", "w") as f:
        json.dump(data, f, indent=4)
