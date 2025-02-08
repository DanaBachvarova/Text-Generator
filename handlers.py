import os
import text_generator
import storage
from typing import List, Optional
from storage import get_corpus_text, list_corpora

CORPUS_DIR = "corpora"
GENERATED_DIR = "generated_texts"

os.makedirs(CORPUS_DIR, exist_ok=True)
os.makedirs(GENERATED_DIR, exist_ok=True)

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
    
def generate_text_with_word(corpus_name: str, uploaded_file: Optional[str], word: str, sentences: int) -> str:
    if not word.strip():
        return "Грешка: Моля, въведете дума за търсене."

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

    return text_generator.generate_text_with_word(corpus_text, word, sentences)

def generate_text_combined(corpus: str, file, word: str, num_sentences: int) -> str:
    word = str(word) if word is not None else ""
    if not word.strip():
        return generate_text(corpus, file, num_sentences)
    return generate_text_with_word(corpus, file, word, num_sentences)