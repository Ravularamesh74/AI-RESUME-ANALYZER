from fastapi import FastAPI, APIRouter, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.analyzer import analyze_resume
from models.response import ResumeResponse

app = FastAPI(title="AI Resume Analyzer", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/api", tags=["Resume Analyzer"])


# Health check
@router.get("/health")
def health_check():
    return {"status": "ok", "message": "API running 🚀"}


# Resume Analysis Endpoint
@router.post("/analyze")
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

    # Return result as-is (with or without error)
    return result


# Include router
app.include_router(router)