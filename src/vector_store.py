from sentence_transformers import (
    SentenceTransformer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

# Load transformer model
model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)


def create_job_embeddings(jobs):

    job_embeddings = []

    # Encode every job
    for job in jobs:

        embedding = model.encode(job)

        job_embeddings.append(
            embedding
        )

    return job_embeddings


def retrieve_top_jobs(
    resume_text,
    jobs,
    job_embeddings,
    top_k=3
):

    # Encode resume
    resume_embedding = model.encode(
        resume_text
    )

    similarity_scores = []

    # Compare against stored vectors
    for i, job_embedding in enumerate(
        job_embeddings
    ):

        similarity = cosine_similarity(
            [resume_embedding],
            [job_embedding]
        )[0][0]

        similarity_scores.append(
            (
                jobs[i],
                round(similarity * 100, 2)
            )
        )

    # Sort descending
    similarity_scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return similarity_scores[:top_k]