from core.logger import logger


def generate_suggestions(score: float, skills: list[str]) -> list[str]:
    """
    Generate improvement suggestions based on score + skills
    """

    suggestions = []

    try:
        # ATS score based suggestions
        if score < 40:
            suggestions.append("Add more role-specific keywords to improve ATS compatibility.")
            suggestions.append("Use clear section headings like Skills, Experience, Projects.")

        elif score < 70:
            suggestions.append("Improve keyword density for better ATS matching.")
            suggestions.append("Align resume more closely with target job descriptions.")

        else:
            suggestions.append("Strong ATS score. Minor optimization may improve visibility.")

        # Skill-based suggestions
        if "python" not in skills:
            suggestions.append("Highlight Python experience if applicable.")

        if len(skills) < 5:
            suggestions.append("Add more measurable technical skills and tools.")

        if "machine learning" not in skills:
            suggestions.append("Consider adding AI/ML-related projects if relevant.")

        # Positive reinforcement
        if score >= 80:
            suggestions.append("Resume looks strong. Focus on quantifying achievements.")

        logger.info(f"Generated {len(suggestions)} suggestions")

        return suggestions

    except Exception:
        logger.exception("Suggestion generation failed")
        return ["Unable to generate suggestions at the moment."]