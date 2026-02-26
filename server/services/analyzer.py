from services.parser import parse_resume
from services.skills import extract_skills
from services.ats import calculate_ats_score
from services.suggestions import generate_suggestions
from core.logger import logger


def analyze_resume(file_bytes: bytes, filename: str) -> dict:
    """
    Main analysis pipeline
    """

    try:
        logger.info(f"Starting analysis for file: {filename}")

        # 1️⃣ Parse resume text
        text = parse_resume(file_bytes, filename)

        if not text or not text.strip():
            logger.warning("Empty resume content detected")
            return {"error": "Unable to extract text from resume"}

        # 2️⃣ Extract skills
        skills = extract_skills(text)
        logger.info(f"Skills extracted: {len(skills)} found")

        # 3️⃣ Calculate ATS score
        score = calculate_ats_score(text)
        logger.info(f"ATS score calculated: {score}")

        # 4️⃣ Generate suggestions
        suggestions = generate_suggestions(score, skills)

        # 5️⃣ Response
        result = {
            "ats_score": score,
            "skills_found": skills,
            "suggestions": suggestions
        }

        logger.info("Resume analysis completed successfully")
        return result

    except Exception as e:
        logger.exception("Resume analysis failed")
        return {"error": f"Analysis failed: {str(e)}"}