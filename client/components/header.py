import streamlit as st
from datetime import datetime

APP_NAME = "🤖 AI Resume Analyzer"


def render_header():
    """
    Modern app header with branding + subtitle
    """

    # Logo
    st.markdown("""
    <div class="ai-float" style="text-align:center;font-size:40px;">
    🤖
    </div>
    """, unsafe_allow_html=True)

    # Title
    st.markdown(
        f"""
        <h1 style='text-align:center; margin-bottom:0;'>
            {APP_NAME}
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Subtitle
    st.markdown(
        """
        <p style='text-align:center; color:gray; font-size:16px;'>
            Analyze your resume with AI • Get ATS score • Improve instantly 🚀
        </p>
        """,
        unsafe_allow_html=True
    )

    # Divider
    st.markdown("---")

    # Small info row
    col1, col2 = st.columns([1, 1])

    with col1:
        st.caption("⚡ FastAPI + Streamlit + NLP")

    with col2:
        st.caption(f"📅 {datetime.now().strftime('%d %b %Y')}")