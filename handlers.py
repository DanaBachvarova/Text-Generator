import os
import text_generator
import storage
from typing import List, Optional

CORPUS_DIR = "corpora"
GENERATED_DIR = "generated_texts"

os.makedirs(CORPUS_DIR, exist_ok=True)
os.makedirs(GENERATED_DIR, exist_ok=True)

def list_corpora() -> List[str]:
    corpora = [f.replace(".txt", "") for f in os.listdir(CORPUS_DIR) if f.endswith(".txt")]
    return ["(Качи нов файл)"] + corpora

def get_corpus_text(name: str) -> Optional[str]:
    path = os.path.join(CORPUS_DIR, f"{name}.txt")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return None

def handle_upload(uploaded_file: Optional[str]):
    if not uploaded_file:
        return "Грешка: Няма качен файл.", list_corpora()
    
    try:
        filename = os.path.basename(uploaded_file)
        new_corpus_path = os.path.join(CORPUS_DIR, filename)
        os.rename(uploaded_file, new_corpus_path)
        return f"Файлът '{filename}' беше качен успешно!", list_corpora()
    except Exception as e:
        return f"Грешка при обработка на файла: {e}", list_corpora()

def generate_text(corpus_name: str, uploaded_file: Optional[str], sentences: int) -> str:
    if corpus_name != "(Качи нов файл)":
        corpus_text = get_corpus_text(corpus_name)
        if not corpus_text:
            return "Грешка: Избраният корпус не съществува."
    elif uploaded_file:
        try:
            with open(uploaded_file, "r", encoding="utf-8") as f:
                corpus_text = f.read()
            filename = os.path.basename(uploaded_file)
            new_corpus_path = os.path.join(CORPUS_DIR, filename)
            os.rename(uploaded_file, new_corpus_path)
        except Exception as e:
            return f"Грешка при обработка на файла: {e}"
    else:
        return "Моля, изберете корпус или качете нов файл."

    return text_generator.generate_text(corpus_text, int(sentences))

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

def list_files() -> str:
    files = storage.list_saved_files()
    return "\n".join(files) if files else "Няма запазени файлове."

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