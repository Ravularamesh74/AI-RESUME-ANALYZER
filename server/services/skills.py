import sys
import warnings
from core.logger import logger

# Suppress pydantic v1 warning for Python 3.14+ compatibility
warnings.filterwarnings("ignore", category=DeprecationWarning, module="pydantic")
warnings.filterwarnings("ignore", message=".*Pydantic V1 functionality.*")

try:
    import spacy
    # Load spaCy model once (fast for API)
    nlp = spacy.load("en_core_web_sm")
except Exception as e:
    logger.warning(f"Failed to load spaCy model: {e}")
    nlp = None

# Known technical skills (expandable)
KNOWN_SKILLS = {
    "python", "java", "c++", "javascript",
    "fastapi", "django", "flask",
    "react", "next.js", "node.js",
    "machine learning", "deep learning",
    "data science", "nlp",
    "sql", "mongodb", "postgresql",
    "docker", "kubernetes", "aws",
    "git", "rest api", "microservices"
}


def extract_skills(text: str) -> list[str]:
    """
    Extract skills using keyword matching
    """

    try:
        found_skills = set()

        # Keyword matching (works with or without NLP)
        for skill in KNOWN_SKILLS:
            if skill in text.lower():
                found_skills.add(skill)

        logger.info(f"Extracted {len(found_skills)} skills")

        return sorted(found_skills)

    except Exception as e:
        logger.exception(f"Skill extraction failed: {e}")
        return []