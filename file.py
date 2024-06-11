import os
import sys
import json

def check_existence(path: str) -> bool:
    return os.path.exists(path)

def create_directory(path: str):
    if not check_existence(path):
        os.makedirs(path)
        print(f"Directory {path} created.")
    else:
        print(f"Directory {path} already exists.")

def add_to_python_path(path: str):
    if path not in sys.path:
        sys.path.append(path)
        print(f"Path {path} added to PYTHONPATH.")

def read_text_file(filepath: str) -> str:
    try:
        with open(filepath, "r", encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return None

def load_json(filepath : str):
    try:
        with open(filepath, "r") as jsonfile:
            json_data = json.load(jsonfile)
        return json_data
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return None

def save_json(filepath: str, data):
    try:
        with open(filepath, "w") as jsonfile:
            json.dump(data, jsonfile, indent=4)
        print(f"Data saved to {filepath}")
    except Exception as e:
        print(f"Error saving data: {e}")

def load_pico(filepath : str):
    with open(filepath, "r") as pico:
        content = list(pico.read())
    return content
