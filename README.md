# 🤖 AI Resume Analyzer

A premium full-stack AI web app that analyzes resumes and provides ATS scores, skill extraction, and smart improvement suggestions using NLP.

Built with **FastAPI + Streamlit + spaCy + AI UI**.

---

## ✨ Features

* 📄 Upload TXT or PDF resumes
* 📊 ATS compatibility score
* 🧠 Automatic skill extraction
* 💡 AI improvement suggestions
* 🎨 Premium animated UI (Neural AI background)
* ⚡ FastAPI backend + Streamlit frontend

---

## 🖼️ Demo

**Frontend:**
http://localhost:8501

**Backend API Docs:**
http://127.0.0.1:8000/docs

---

## 🧠 Tech Stack

### Frontend

* Streamlit
* Custom CSS (Glassmorphism + AI animations)
* Neural particle background

### Backend

* FastAPI
* spaCy (NLP)
* Scikit-learn (ATS scoring)
* PyPDF2 (PDF parsing)

---

## 📁 Project Structure

```
AI-Resume-Analyzer/
client/
│
├── app.py                 # Main Streamlit UI
├── api.py                 # Backend API handler (optional but clean)
├── config.py              # API URLs and constants
├── utils/
│   ├── file_handler.py    # Resume file validation
│   └── helpers.py         # UI helper functions
│
├── components/
│   ├── header.py          # Title + branding
│   ├── uploader.py        # File upload UI
│   ├── results.py         # Score + results display
│   └── suggestions.py     # Suggestions UI
│
├── assets/
│   ├── logo.png
│   └── styles.css         # Custom styling (optional)
│
├── requirements.txt
server/
│
├── app/
│   ├── main.py              # FastAPI entry
│   ├── api/
│   │   └── routes.py        # API endpoints
│   │
│   ├── core/
│   │   ├── config.py        # Settings
│   │   └── logger.py        # Logging
│   │
│   ├── services/
│   │   ├── analyzer.py      # Orchestrator
│   │   ├── parser.py        # TXT/PDF parsing
│   │   ├── skills.py        # NLP skill extraction
│   │   ├── ats.py           # ATS scoring
│   │   └── suggestions.py   # AI suggestions
│   │
│   ├── models/
│   │   └── response.py      # Pydantic schemas
│   │
│   └── utils/
│       └── file_utils.py
│
├── requirements.txt
└── README.md

---

## 🚀 Installation

### 1️⃣ Clone Repo

```bash
git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r server/requirements.txt
pip install -r client/requirements.txt
```

---

### 4️⃣ Install spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

## ▶️ Run the App

### Start Backend

```bash
cd server
uvicorn app.main:app --reload
```

---

### Start Frontend (new terminal)

```bash
cd client
streamlit run app.py
```

---

## 🌐 Usage

1. Upload your resume (PDF/TXT)
2. Click **Analyze Resume**
3. View:

   * ATS Score
   * Detected Skills
   * AI Suggestions

---

## 🎨 UI Highlights

* Neural AI animated background
* Blue premium SaaS theme
* Floating AI elements
* Smooth animations

---

## 📊 Example Output

```json
{
  "ats_score": 82.3,
  "skills_found": ["python", "fastapi", "docker"],
  "suggestions": [
    "Improve keyword density",
    "Add measurable achievements"
  ]
}
```

---

## 🔮 Future Improvements

* 🤖 OpenAI/Gemini integration
* 📊 Skill radar charts
* 📄 Downloadable PDF reports
* 🌙 Dark mode
* 🌐 Cloud deployment

---

## 📦 Deployment Options

* Streamlit Cloud
* Render / Railway
* Docker container

---

## 🙋 Author

**Ramesh Ravula**
📍 Hyderabad, India
🎓 MCA Student
💻 AI & Full-Stack Developer

---

## ⭐ Support

If you like this project:

⭐ Star the repo
🍴 Fork it
📢 Share it

---

## 📜 License

MIT License — free to use and modify.
