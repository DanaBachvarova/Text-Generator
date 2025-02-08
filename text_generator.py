import markovify

def load_corpus(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()
    
def generate_text(corpus, sentences=5):
    model = markovify.Text(corpus, state_size=2)
    generated_sentences = []
    for _ in range(sentences):
        sentence = model.make_sentence()
        if sentence:
            generated_sentences.append(sentence)
    return " ".join(generated_sentences)