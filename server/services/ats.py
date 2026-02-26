from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Default target role (can be dynamic later)
DEFAULT_JOB_DESCRIPTION = """
Python developer with experience in backend development,
FastAPI, machine learning, APIs, and scalable systems.
"""


def calculate_ats_score(resume_text: str, job_description: str = DEFAULT_JOB_DESCRIPTION) -> float:
    """
    Calculate ATS compatibility score using semantic similarity
    """

    try:
        documents = [resume_text, job_description]

        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform(documents)

        similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

        # Convert to percentage
        score = round(similarity * 100, 2)

        return score

    except Exception:
        return 0.0