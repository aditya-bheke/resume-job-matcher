import nltk
import string
import spacy

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")

nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):
    text = text.lower()

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words("english"))

    filtered_tokens = []

    for word in tokens:
        if word not in stop_words and word not in string.punctuation:
            filtered_tokens.append(word)

    cleaned_text = " ".join(filtered_tokens)

    doc = nlp(cleaned_text)

    lemmatized_tokens = []

    for token in doc:
        lemmatized_tokens.append(token.lemma_)

    final_text = " ".join(lemmatized_tokens)

    return final_text