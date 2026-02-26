import streamlit as st

def show_error(message):
    """Display error message"""
    st.error(message)


def show_success(message):
    """Display success message"""
    st.success(message)


def show_warning(message):
    """Display warning message"""
    st.warning(message)


def show_metric(label, value):
    """Display metric card"""
    st.metric(label, value)


def show_spinner(text="Processing..."):
    """Reusable spinner"""
    return st.spinner(text)


def section_title(title, icon="📌"):
    """Styled section title"""
    st.markdown(f"### {icon} {title}")


def divider():
    """UI divider"""
    st.markdown("---")