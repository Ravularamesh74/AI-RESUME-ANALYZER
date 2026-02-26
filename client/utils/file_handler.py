import os

ALLOWED_EXTENSIONS = ["txt"]  # later add pdf

def validate_file(uploaded_file):
    """
    Validate uploaded resume file
    Returns (is_valid, message)
    """

    if uploaded_file is None:
        return False, "Please upload a resume file."

    filename = uploaded_file.name.lower()

    # Check extension
    if not any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS):
        return False, "Only TXT files are supported."

    # File size check (max 2MB)
    uploaded_file.seek(0, os.SEEK_END)
    size = uploaded_file.tell()
    uploaded_file.seek(0)

    if size > 2 * 1024 * 1024:
        return False, "File too large (Max 2MB)."

    return True, ""