from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional


class ResumeResponse(BaseModel):
    """
    Response schema for resume analysis
    """
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "ats_score": 82.3,
                "skills_found": ["python", "machine learning", "fastapi"],
                "suggestions": [
                    "Add more measurable achievements",
                    "Improve keyword density for ATS"
                ],
                "error": None
            }
        }
    )

    ats_score: float = Field(..., example=78.5, description="ATS compatibility score")
    skills_found: List[str] = Field(
        default_factory=list,
        example=["python", "fastapi", "sql"],
        description="Extracted skills from resume",
    )
    suggestions: List[str] = Field(
        default_factory=list,
        example=["Add more AI-related keywords"],
        description="Improvement suggestions",
    )
    error: Optional[str] = Field(
        default=None,
        description="Error message if processing failed",
    )