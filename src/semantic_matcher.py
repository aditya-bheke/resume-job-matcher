from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load pretrained Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')


def calculate_semantic_match(resume_text, job_text):

    # Convert texts into semantic embeddings
    embeddings = model.encode([resume_text, job_text])

    # Calculate cosine similarity
    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )

    # Return percentage score
    return round(similarity[0][0] * 100, 2)