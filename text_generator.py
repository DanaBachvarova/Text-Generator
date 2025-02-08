'''
Module for generating text using a Markov chain model based on a given corpus.
Provides functions for generating text with or without a specific keyword.
'''
import markovify

def generate_text(corpus: str, sentences: int) -> str:
    '''
    Generates a specified number of sentences using a Markov chain model 
    based on the given corpus.
    
    Parameters:
    corpus (str): The text corpus used to train the Markov chain model.
    sentences (int): The number of sentences to generate.
    
    Returns:
    str: A string of generated sentences.
    '''
    model = markovify.Text(corpus, state_size=2)
    generated_sentences = []
    for _ in range(sentences):
        sentence = model.make_sentence()
        if sentence:
            generated_sentences.append(sentence)
    return " ".join(generated_sentences)

def generate_text_with_word(corpus: str, keyword: str, sentences: int) -> str:
    '''
    Generates a specified number of sentences using a Markov chain model, 
    ensuring that each sentence contains a specific keyword.
    
    Parameters:
    corpus (str): The text corpus used to train the Markov chain model.
    keyword (str): The word that must appear in each generated sentence.
    sentences (int): The number of sentences to generate.
    
    Returns:
    str: A string of generated sentences containing the keyword, 
    or an error message if no such sentences are found.
    '''
    model = markovify.Text(corpus, state_size=2)
    generated_sentences = []
    attempts = 0
    while len(generated_sentences) < sentences and attempts < 50:
        sentence = model.make_sentence()
        if sentence and keyword.lower() in sentence.lower():
            generated_sentences.append(sentence)
        attempts += 1

    if not generated_sentences:
        return "Не можах да генерирам изречения с тази дума."

    return " ".join(generated_sentences)
