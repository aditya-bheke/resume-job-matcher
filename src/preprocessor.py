import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")


def preprocess_text(text):
    text = text.lower()

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words("english"))

    filtered_tokens = []

    for word in tokens:
        if word not in stop_words and word not in string.punctuation:
            filtered_tokens.append(word)

    cleaned_text = " ".join(filtered_tokens)

    return cleaned_text