import re

def clean_text(text):
    # Lowercase and remove non-alphanumeric characters
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

def tokenize(text):
    text = clean_text(text)
    return text.split()
