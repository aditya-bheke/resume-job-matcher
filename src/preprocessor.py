# NLTK for tokenization and stopword removal
import nltk

# Used for punctuation symbols
import string

# spaCy for lemmatization
import spacy

# Stopword list from NLTK
from nltk.corpus import stopwords

# Tokenizer from NLTK
from nltk.tokenize import word_tokenize


# Download tokenizer model
nltk.download("punkt")

# Additional tokenizer dependency
nltk.download("punkt_tab")

# Download stopword dataset
nltk.download("stopwords")


# Load spaCy English NLP model
nlp = spacy.load("en_core_web_sm")


# Main preprocessing function
def preprocess_text(text):

    # Convert text to lowercase
    # Prevents Python/PYTHON/python mismatch
    text = text.lower()

    # Split sentence into words/tokens
    tokens = word_tokenize(text)

    # Load English stopwords
    stop_words = set(stopwords.words("english"))

    # Store cleaned tokens
    filtered_tokens = []

    # Loop through every token
    for word in tokens:

        # Remove stopwords and punctuation
        if word not in stop_words and word not in string.punctuation:

            # Keep meaningful words only
            filtered_tokens.append(word)

    # Convert tokens back into sentence
    cleaned_text = " ".join(filtered_tokens)

    # Pass cleaned text into spaCy NLP pipeline
    doc = nlp(cleaned_text)

    # Store lemmatized/root words
    lemmatized_tokens = []

    # Loop through every processed token
    for token in doc:

        # Extract root/base word
        lemmatized_tokens.append(token.lemma_)

    # Convert root words back into sentence
    final_text = " ".join(lemmatized_tokens)

    # Return fully cleaned text
    return final_text