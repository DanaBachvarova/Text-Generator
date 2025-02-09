'''
Module for managing text file operations such as saving generated text, 
retrieving corpus text,
and listing saved files and available corpora.
'''
import os
from typing import Optional, List

CORPUS_DIR = "corpora"
GENERATED_DIR = "generated_texts"

def save_generated_text(text: str, filename: Optional[str]) -> str:
    '''
    Saves the generated text to a file. If no filename is provided, 
    it generates a unique one.
    
    Parameters:
    text (str): The generated text to be saved.
    filename (Optional[str]): The name of the file to save the text to. 
    If None, a unique filename is created.
    
    Returns:
    str: A message indicating whether the text was successfully saved or 
    if there was an error.
    '''
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
    '''
    Retrieves the content of a corpus text file by name.
    
    Parameters:
    name (str): The name of the corpus file to retrieve (without the .txt extension).
    
    Returns:
    Optional[str]: The content of the corpus file, or None if the file does not exist.
    '''
    path = os.path.join(CORPUS_DIR, f"{name}.txt")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return None

def list_saved_files() -> str:
    '''
    Lists all saved text files in the generated texts directory.
    
    Returns:
    str: A string containing the names of the saved files, 
    or a message indicating there are no saved files.
    '''
    files = [f for f in os.listdir("generated_texts") if f.endswith(".txt")]
    return "\n".join(files) if files else "Няма запазени файлове."

def list_saved_files_dropdown() -> List[str]:
    '''
    Returns a list of saved text files in the "generated_texts" directory.

    Returns:
    List[str]: A list of filenames ending with ".txt".
    '''
    return [f for f in os.listdir("generated_texts") if f.endswith(".txt")]

def list_corpora() -> List[str]:
    '''
    Lists the names of all available corpora files (without the .txt extension).
    
    Returns:
    List[str]: A list of corpus names, including an option to upload a new file.
    '''
    corpora = [f.replace(".txt", "") for f in os.listdir(CORPUS_DIR) if f.endswith(".txt")]
    return ["(Качи нов файл)"] + corpora
