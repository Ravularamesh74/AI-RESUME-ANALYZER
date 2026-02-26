import streamlit as st


def render_results(data: dict):
    """
    Display ATS score and detected skills
    """

    if not data:
        st.error("No results available.")
        return

    score = data.get("ats_score", 0)
    skills = data.get("skills_found", [])

    # =========================
    # ATS SCORE SECTION
    # =========================
    st.markdown("## 📊 ATS Score")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.metric("Score", f"{score}%")

    with col2:
        # Progress bar
        st.progress(min(score / 100, 1.0))

        if score >= 80:
            st.success("Excellent ATS compatibility 🎉")
        elif score >= 60:
            st.info("Good score — small improvements possible 👍")
        else:
            st.warning("Low ATS score — optimization recommended ⚠️")

    st.markdown("---")

    # =========================
    # SKILLS SECTION
    # =========================
    st.markdown("## 🧠 Detected Skills")

    if skills:
        # Skill badges
        badge_html = " ".join(
            f"<span style='background:#f0f2f6;padding:6px 10px;border-radius:8px;margin:4px;display:inline-block'>{skill}</span>"
            for skill in skills
        )
        st.markdown(badge_html, unsafe_allow_html=True)
    else:
        st.warning("No skills detected.")

    st.markdown("---")