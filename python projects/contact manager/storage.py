import json

def load_contacts():
    try:
        with open("contacts.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def save_contacts(data):
    with open("contacts.json", "w") as f:
        json.dump(data, f, indent=4)
