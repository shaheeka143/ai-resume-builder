import spacy
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text.lower())
    return list(set(
        token.text for token in doc
        if token.pos_ in ["NOUN", "PROPN", "ADJ"] and len(token.text) > 2
    ))
