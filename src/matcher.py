# TF-IDF vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Cosine similarity calculator
from sklearn.metrics.pairwise import cosine_similarity


# Main similarity function
def calculate_match(resume_text, job_text):

    # Store resume and job inside list
    documents = [resume_text, job_text]

    # Create TF-IDF vectorizer object
    vectorizer = TfidfVectorizer()

    # Convert text documents into numerical vectors
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Calculate cosine similarity between resume and job vectors
    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    # Convert similarity score into percentage
    # Round to 2 decimal places
    return round(similarity[0][0] * 100, 2)