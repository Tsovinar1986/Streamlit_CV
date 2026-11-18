"""Streamlit host for the CV website.

The page is index.html at the repo root (also served by GitHub Pages at
https://tsovinar1986.github.io/Streamlit_CV/). Edit index.html and push.
"""
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).parent

st.set_page_config(
    page_title="Tsovinar Babakhanyan | ML & NLP Engineer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's chrome so the CV fills the page.
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], footer, #MainMenu {display:none !important;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {display:block; border:0;}
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def build_page() -> str:
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    photo = base64.b64encode((ROOT / "site" / "photo.jpg").read_bytes()).decode()
    # The iframe can't load relative files, so inline the photo.
    return html.replace('src="site/photo.jpg"', f'src="data:image/jpeg;base64,{photo}"')


components.html(build_page(), height=6400, scrolling=True)

pdf = ROOT / "Tsovinar_Babakhanyan_Optimized_CV.pdf"
if pdf.exists():
    st.download_button("Download CV (PDF)", pdf.read_bytes(), file_name=pdf.name, mime="application/pdf")
