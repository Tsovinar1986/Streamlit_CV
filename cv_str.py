import streamlit as st

st.set_page_config(
    page_title="Tsovinar Babakhanyan | Technical CV",
    page_icon="🧠",
    layout="wide"
)

# ---------- HEADER ----------
st.title("👩‍💻 Tsovinar Tina Babakhanyan")
st.subheader("Data Scientist | Machine Learning & NLP Engineer")

col1, col2, col3 = st.columns(3)
col1.write("📍 Armenia")
col2.write("📧 Tsovinar.babakhanyan@hotmail.com")
col3.markdown("🔗 [GitHub](https://github.com/Tsovinar1986) | [DAGsHub](https://dagshub.com/Tsovinar1986)")

st.markdown("---")

# ---------- SUMMARY ----------
st.markdown("### 🧠 Professional Summary")
st.write(
    """
    Data Scientist and Junior Machine Learning Engineer with hands-on experience in 
    **NLP, LLMs, and real-world AI projects**. Worked on multilingual NLP, chatbots,
    and data analytics through **Omdena and startup environments**.
    """
)

# ---------- SKILLS ----------
st.markdown("### 🛠 Technical Skills")
skills_col1, skills_col2 = st.columns(2)

skills_col1.markdown("""
- **Languages:** Python, SQL  
- **ML / AI:** NLP, LLMs, Transformers  
- **Frameworks:** PyTorch, TensorFlow, Hugging Face  
- **LLM Tools:** LangChain, CrewAI
""")

skills_col2.markdown("""
- **Data:** Pandas, NumPy, GeoPandas, QGIS  
- **CV:** OpenCV  
- **Web:** Flask, Django (basic)  
- **Tools:** Git, GitHub, Azure DevOps, Jira, TestRail, Postman
""")

# ---------- EXPERIENCE ----------
st.markdown("### 💼 Experience")

with st.expander("Omdena – Junior Machine Learning Engineer (Oct 2024 – Dec 2024)"):
    st.markdown("""
    - Built NLP & LLM-based WhatsApp chatbot solutions  
    - Led image & text preprocessing pipelines  
    - Applied OpenCV for exercise classification
    """)

with st.expander("Oragic Startup – Data Science Intern (Sep 2022 – Dec 2023)"):
    st.markdown("""
    - Multilingual NLP research (DE, FR, ES, IT, ZH, EN)  
    - Sentiment analysis & text classification models
    """)

# ---------- EDUCATION ----------
st.markdown("### 🎓 Education")

st.markdown("""
**Master’s Degree – Computer Engineering (2008–2009)**  
Fast Layer-3 Handover in Vehicular Networks  

**Bachelor’s Degree – Computer Complexes and Networks (2003–2007)**
""")

# ---------- CERTIFICATIONS ----------
st.markdown("### 📜 Certifications")

st.markdown("""
- Product Owner – Omdena  
- Data Engineer – Omdena  
- AI Innovation Challenge  
- Text Summarization – Omdena  
- QA Methodologies  
- Python Developer & Machine Learning
""")

# ---------- LANGUAGES ----------
st.markdown("### 🌍 Languages")

st.markdown("""
- Armenian – Native  
- English – Advanced  
- Russian – Intermediate
""")

# ---------- DOWNLOAD CV ----------
st.markdown("---")
st.markdown("### 📄 Download CV")

with open("Tsovinar_Babakhanyan_CV.pdf", "rb") as file:
    st.download_button(
        label="⬇️ Download PDF CV",
        data=file,
        file_name="Tsovinar_Babakhanyan_CV.pdf",
        mime="application/pdf"
    )

# ---------- FOOTER ----------
st.markdown("---")
st.caption("© 2026 Tsovinar Babakhanyan | Streamlit Technical CV")
