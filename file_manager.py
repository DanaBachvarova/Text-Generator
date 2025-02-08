import os

CORPUS_DIR = "corpora"
GENERATED_DIR = "generated_texts"

def open_file(filename: str) -> str:
    try:
        with open(os.path.join(GENERATED_DIR, filename), "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Грешка: Файлът не е намерен."

def delete_file(filename: str) -> str:
    try:
        os.remove(os.path.join(GENERATED_DIR, filename))
        return f"Файлът '{filename}' беше изтрит успешно."
    except FileNotFoundError:
        return "Грешка: Файлът не е намерен."