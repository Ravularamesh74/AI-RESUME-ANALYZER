import streamlit as st


def render_suggestions(suggestions: list[str]):
    """
    Display AI suggestions in a modern card layout
    """

    st.markdown("## 💡 AI Suggestions")

    if not suggestions:
        st.success("Great resume! No major improvements needed 🎉")
        st.markdown("---")
        return

    # Render suggestions as cards
    for tip in suggestions:
        st.markdown(
            f"""
            <div style="
                background-color:#f9fafb;
                padding:12px 16px;
                border-radius:10px;
                margin-bottom:10px;
                border-left:4px solid #4CAF50;
            ">
                {tip}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")