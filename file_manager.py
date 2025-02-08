'''
Module for handling file operations related to corpora and generated texts.
Includes functionality to open and delete files from the generated texts directory.
'''
import os

GENERATED_DIR = "generated_texts"

def open_file(filename: str) -> str:
    '''
    Opens a file from the generated texts directory and returns its content as a string.
    
    Parameters:
    filename (str): The name of the file to open.
    
    Returns:
    str: The content of the file, or an error message if the file is not found.
    '''
    try:
        with open(os.path.join(GENERATED_DIR, filename), "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Грешка: Файлът не е намерен."

def delete_file(filename: str) -> str:
    '''
    Deletes a file from the generated texts directory.
    
    Parameters:
    filename (str): The name of the file to delete.
    
    Returns:
    str: A success message if the file is deleted, or an error message if the file is not found.
    '''
    try:
        os.remove(os.path.join(GENERATED_DIR, filename))
        return f"Файлът '{filename}' беше изтрит успешно."
    except FileNotFoundError:
        return "Грешка: Файлът не е намерен."
