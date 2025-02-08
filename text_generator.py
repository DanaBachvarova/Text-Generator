import markovify
from typing import Optional

def generate_text(corpus: str, sentences: int) -> str:
    model = markovify.Text(corpus, state_size=2)
    generated_sentences = []
    for _ in range(sentences):
        sentence = model.make_sentence()
        if sentence:
            generated_sentences.append(sentence)
    return " ".join(generated_sentences)

def generate_text_with_word(corpus: str, keyword: str, sentences: int) -> str:
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
