from fastapi import APIRouter, UploadFile, File, HTTPException
from services.analyzer import analyze_resume
from models.response import ResumeResponse

router = APIRouter(prefix="/api", tags=["Resume Analyzer"])


# Health check
@router.get("/health")
def health_check():
    return {"status": "ok", "message": "API running 🚀"}


# Resume Analysis Endpoint
@router.post("/analyze", response_model=ResumeResponse)
async def analyze(file: UploadFile = File(...)):
    """
    Upload resume and get ATS analysis
    Supports TXT and PDF
    """

    # Validate file type
    allowed_types = (".txt", ".pdf")
    if not file.filename.lower().endswith(allowed_types):
        raise HTTPException(
            status_code=400,
            detail="Only TXT and PDF files are supported."
        )

    # Read file
    try:
        content = await file.read()
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to read file.")

    # File empty check
    if not content:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    # Analyze resume
    result = analyze_resume(content, file.filename)

    # Handle analyzer errors
    if "error" in result:
        raise HTTPException(status_code=422, detail=result["error"])

    return result