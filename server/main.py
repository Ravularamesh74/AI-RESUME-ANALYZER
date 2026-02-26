from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import spacy
import fitz  # PyMuPDF
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

app = FastAPI(title="AI Resume Analyzer")

# CORS (important for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Utility Functions
# -------------------------------

def extract_text_from_pdf(file_bytes: bytes) -> str:
    text = ""
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text


def extract_skills(text: str):
    skills_list = [
        "python", "java", "javascript", "react", "node", "sql",
        "machine learning", "deep learning", "nlp", "fastapi",
        "django", "flask", "aws", "docker", "kubernetes"
    ]
    found = []
    lower_text = text.lower()
    for skill in skills_list:
        if skill in lower_text:
            found.append(skill)
    return found


def extract_email(text: str):
    match = re.search(r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+", text)
    return match.group(0) if match else None


def extract_phone(text: str):
    match = re.search(r"\+?\d[\d\s\-]{8,15}", text)
    return match.group(0) if match else None


def calculate_score(skills):
    base = len(skills) * 10
    return min(base, 100)


# -------------------------------
# Routes
# -------------------------------

@app.get("/")
def home():
    return {"message": "AI Resume Analyzer API Running 🚀"}


@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    try:
        content = await file.read()

        # Extract text
        text = extract_text_from_pdf(content)

        # NLP processing
        doc = nlp(text)

        skills = extract_skills(text)
        email = extract_email(text)
        phone = extract_phone(text)
        score = calculate_score(skills)

        return JSONResponse({
            "success": True,
            "score": score,
            "email": email,
            "phone": phone,
            "skills": skills,
            "summary": text[:500]
        })

    except Exception as e:
        return JSONResponse({
            "success": False,
            "error": str(e)
        }, status_code=500)