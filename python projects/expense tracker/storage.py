import json

def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def save_expenses(data):
    with open("expenses.json", "w") as f:
        json.dump(data, f, indent=4)
