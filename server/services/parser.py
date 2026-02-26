import io
from PyPDF2 import PdfReader
from core.logger import logger


def parse_resume(file_bytes: bytes, filename: str) -> str:
    """
    Extract text from resume based on file type
    """

    try:
        filename = filename.lower()

        if filename.endswith(".pdf"):
            return _parse_pdf(file_bytes)

        elif filename.endswith(".txt"):
            return file_bytes.decode("utf-8", errors="ignore")

        else:
            logger.warning(f"Unsupported file format: {filename}")
            return ""

    except Exception as e:
        logger.exception("Resume parsing failed")
        return ""


# -----------------------------
# PDF Parser
# -----------------------------
def _parse_pdf(file_bytes: bytes) -> str:
    """
    Extract text from PDF using PyPDF2
    """
    text = ""

    try:
        reader = PdfReader(io.BytesIO(file_bytes))

        for page_num, page in enumerate(reader.pages):
            page_text = page.extract_text() or ""
            text += page_text + "\n"

        logger.info("PDF parsed successfully")
        return text.strip()

    except Exception:
        logger.exception("PDF parsing error")
        return ""