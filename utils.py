import json

def save_data(data):
    with open("students.json", "w") as f:
        json.dump(data, f, indent=2)

def load_data():
    with open("students.json", "r") as f:
        return json.load(f)