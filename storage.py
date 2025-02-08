import json
import os
from typing import Optional, List

CORPUS_DIR = "corpora"
GENERATED_DIR = "generated_texts"

def save_generated_text(text: str, filename: Optional[str]) -> str:
    if not text.strip():
        return "Грешка: Генерираният текст е празен и няма да бъде запазен."

    if not filename:
        counter = 1
        while os.path.exists(os.path.join(GENERATED_DIR, f"generated_text_{counter}.txt")):
            counter += 1
        filename = f"generated_text_{counter}.txt"
    
    filepath = os.path.join(GENERATED_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(text)
    
    return f"Текстът е запазен като {filename}"

def get_corpus_text(name: str) -> Optional[str]:
    path = os.path.join(CORPUS_DIR, f"{name}.txt")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return None
    
def list_saved_files() -> str:
    files = [f for f in os.listdir("generated_texts") if f.endswith(".txt")]
    return "\n".join(files) if files else "Няма запазени файлове."

def list_corpora() -> List[str]:
    corpora = [f.replace(".txt", "") for f in os.listdir(CORPUS_DIR) if f.endswith(".txt")]
    return ["(Качи нов файл)"] + corpora