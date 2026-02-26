import streamlit as st


def render_uploader():
    """
    Resume upload component
    Supports TXT and PDF
    """

    st.markdown("## 📄 Upload Your Resume")

    st.caption("Supported formats: TXT, PDF • Max size ~5MB")

    uploaded_file = st.file_uploader(
        label="Choose your resume file",
        type=["txt", "pdf"],
        help="Upload a resume to analyze ATS score and skills"
    )

    if uploaded_file:
        file_details = {
            "filename": uploaded_file.name,
            "size_kb": round(uploaded_file.size / 1024, 2),
            "type": uploaded_file.type
        }

        st.info(
            f"📁 **{file_details['filename']}**  \n"
            f"Size: {file_details['size_kb']} KB"
        )

    st.markdown("---")

    return uploaded_file