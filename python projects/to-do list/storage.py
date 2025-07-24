import json

def load_tasks():
    try:
        with open("todos.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def save_tasks(data):
    with open("todos.json", "w") as f:
        json.dump(data, f, indent=4)
