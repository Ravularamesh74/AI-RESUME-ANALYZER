"""
Utility configuration for frontend
Used across utils, API layer, and components
"""

# ==============================
# API CONFIG
# ==============================
API_BASE_URL = "http://127.0.0.1:8000/api"
ANALYZE_API = f"{API_BASE_URL}/analyze"
HEALTH_API = f"{API_BASE_URL}/health"

# ==============================
# FILE VALIDATION
# ==============================
ALLOWED_EXTENSIONS = ["txt", "pdf"]
MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

# ==============================
# UI CONSTANTS
# ==============================
APP_TITLE = "AI Resume Analyzer"
APP_ICON = "🤖"

SUCCESS_MESSAGES = {
    "upload": "File uploaded successfully",
    "analysis": "Resume analyzed successfully"
}

ERROR_MESSAGES = {
    "backend_down": "Backend not running. Start FastAPI server.",
    "invalid_file": "Unsupported file format.",
    "file_large": f"File too large (Max {MAX_FILE_SIZE_MB}MB)",
    "empty_file": "Uploaded file is empty."
}

# ==============================
# NETWORK SETTINGS
# ==============================
REQUEST_TIMEOUT = 60  # seconds