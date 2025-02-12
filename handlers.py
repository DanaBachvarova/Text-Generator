'''
Module for handling file uploads, text generation, and corpus management.
Includes functionality for uploading files, generating text from a corpus,
and generating text with specific words from a given corpus.
'''
import os
from typing import Optional
import text_generator
from storage import get_corpus_text

CORPUS_DIR = "corpora"
GENERATED_DIR = "generated_texts"

os.makedirs(CORPUS_DIR, exist_ok=True)
os.makedirs(GENERATED_DIR, exist_ok=True)

def generate_text(corpus_name: str, uploaded_file: Optional[str], sentences: int) -> str:
    '''
    Generates text based on a selected corpus or an uploaded file.

    Parameters:
    corpus_name (str): The name of the selected corpus.
    uploaded_file (str, optional): The path to the uploaded file.
    sentences (int): The number of sentences to generate.

    Returns:
    str: The generated text or an error message.
    '''
    if corpus_name != "(Качи нов файл)":
        corpus_text = get_corpus_text(corpus_name)
    elif uploaded_file:
        try:
            with open(uploaded_file, "r", encoding="utf-8") as f:
                corpus_text = f.read()
            filename = os.path.basename(uploaded_file)
            new_corpus_path = os.path.join(CORPUS_DIR, filename)
            os.rename(uploaded_file, new_corpus_path)
        except FileNotFoundError:
            return "Грешка: Файлът не беше намерен."
        except UnicodeDecodeError:
            return "Грешка: Невалиден формат на файла."
        except IOError as e:
            return f"Грешка при отваряне на файла: {e}"
    else:
        return "Моля, изберете корпус или качете нов файл."

    return text_generator.generate_text(corpus_text, int(sentences))

def generate_text_with_word(corpus_name: str, uploaded_file: Optional[str],
                            word: str, sentences: int) -> str:
    '''
    Generates text based on a selected corpus or an uploaded file, 
    ensuring the presence of a specific word.

    Parameters:
    corpus_name (str): The name of the selected corpus.
    uploaded_file (str, optional): The path to the uploaded file.
    word (str): The word that must be present in the generated sentences.
    sentences (int): The number of sentences to generate.

    Returns:
    str: The generated text containing the specified word or an error message.
    '''
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
        except FileNotFoundError:
            return "Грешка: Файлът не беше намерен."
        except UnicodeDecodeError:
            return "Грешка: Невалиден формат на файла."
        except IOError as e:
            return f"Грешка при отваряне на файла: {e}"
    else:
        return "Моля, изберете корпус или качете нов файл."

    return text_generator.generate_text_with_word(corpus_text, word, sentences)

def generate_text_combined(corpus: str, file, word: str, num_sentences: int) -> str:
    '''
    Combines text generation with or without a specific word, 
    based on the corpus and user input.

    Parameters:
    corpus (str): The name of the selected corpus.
    file (str, optional): The path to the uploaded file.
    word (str): The word that may be present in the generated sentences.
    num_sentences (int): The number of sentences to generate.

    Returns:
    str: The generated text, either with or without the specified word.
    '''
    word = str(word) if word is not None else ""
    if not word.strip():
        return generate_text(corpus, file, num_sentences)
    return generate_text_with_word(corpus, file, word, num_sentences)
