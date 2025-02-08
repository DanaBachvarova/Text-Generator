import json
import os

def save_text(text, filename="generated_texts.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    
    data.append(text)
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_texts(filename="generated_texts.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def list_saved_files() -> str:
    files = [f for f in os.listdir("generated_texts") if f.endswith(".txt")]
    return "\n".join(files) if files else "Няма запазени файлове."