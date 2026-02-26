
import streamlit as st

# Components
from components.header import render_header
from components.uploader import render_uploader
from components.results import render_results
from components.suggestions import render_suggestions

# API
from api import analyze_resume

# Page Config
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="centered"
)

# Initialize session state
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

# Load styles
def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ==============================
# HEADER
# ==============================
render_header()

# ==============================
# FILE UPLOAD
# ==============================
uploaded_file = render_uploader()

# ==============================
# ANALYZE BUTTON
# ==============================
if uploaded_file:
    if st.button("🚀 Analyze Resume", use_container_width=True):

        with st.spinner("Analyzing your resume... 🤖"):

            file_bytes = uploaded_file.getvalue()
            filename = uploaded_file.name

            data = analyze_resume(file_bytes, filename)
            
            print(f"DEBUG: Received data from backend: {data}")

            # ==============================
            # ERROR HANDLING
            # ==============================
            if not data:
                st.error("❌ No response from server.")
                st.session_state.analysis_result = None
            elif "error" in data:
                st.error(f"❌ {data['error']}")
                st.session_state.analysis_result = None
            else:
                # Store result in session state
                st.session_state.analysis_result = data
                st.success("✅ Resume analyzed successfully!")

    # Display results if they exist in session state
    if st.session_state.analysis_result:
        st.markdown("---")
        
        print(f"DEBUG: Displaying results: {st.session_state.analysis_result}")
        
        # ==============================
        # RESULTS
        # ==============================
        render_results(st.session_state.analysis_result)

        # ==============================
        # SUGGESTIONS
        # ==============================
        render_suggestions(st.session_state.analysis_result.get("suggestions", []))
else:
    st.info("📤 Please upload your resume to get started!")
