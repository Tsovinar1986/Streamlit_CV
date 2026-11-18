"""Streamlit host for the CV website.

The page itself lives in site/cv.html (photo in site/photo.jpg). Edit those
files and push; Streamlit Community Cloud redeploys automatically.
"""
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).parent
SITE = ROOT / "site"

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
    html = (SITE / "cv.html").read_text(encoding="utf-8")
    photo = base64.b64encode((SITE / "photo.jpg").read_bytes()).decode()
    html = html.replace("__PHOTO__", photo)
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        "<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>"
        f"</head><body>{html}</body></html>"
    )


components.html(build_page(), height=5600, scrolling=True)

# Keep the original PDF CV downloadable.
pdf = ROOT / "Tsovinar_Babakhanyan_CV.pdf"
if pdf.exists():
    st.download_button("Download CV (PDF)", pdf.read_bytes(), file_name=pdf.name, mime="application/pdf")
