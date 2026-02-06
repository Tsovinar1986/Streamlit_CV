import streamlit as st
import base64

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Tsovinar Babakhanyan | Technical CV",
    page_icon="🧠",
    layout="wide"
)

# ================= HEADER =================
st.title("👩‍💻 Tsovinar Tina Babakhanyan")
st.subheader("Data Scientist | Machine Learning & NLP Engineer")

col1, col2, col3 = st.columns(3)
col1.write("📍 Armenia")
col2.write("📧 Tsovinar.babakhanyan@hotmail.com")
col3.markdown(
    "🔗 [GitHub](https://github.com/Tsovinar1986) | "
    "[DAGsHub](https://dagshub.com/Tsovinar1986)"
)

st.markdown("---")

# ================= SUMMARY =================
st.markdown("### 🧠 Professional Summary")
st.write(
    """
    Data Scientist and Junior Machine Learning Engineer with hands-on experience in  
    **NLP, LLMs, and real-world AI projects**.

    Experienced in multilingual NLP, chatbots, and data analytics through  
    **Omdena and startup environments**.
    """
)

# ================= SKILLS =================
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

# ================= EXPERIENCE =================
st.markdown("### 💼 Experience")

with st.expander("Omdena – Junior Machine Learning Engineer (Oct 2024 – Dec 2024)"):
    st.markdown("""
    - Built NLP & LLM-based WhatsApp chatbot solutions  
    - Image & text preprocessing pipelines  
    - OpenCV-based exercise classification
    """)

with st.expander("Oragic Startup – Data Science Intern (Sep 2022 – Dec 2023)"):
    st.markdown("""
    - Multilingual NLP research (DE, FR, ES, IT, ZH, EN)  
    - Sentiment analysis & text classification models
    """)

# ================= EDUCATION =================
st.markdown("### 🎓 Education")

st.markdown("""
**Master’s Degree – Computer Engineering (2008–2009)**  
Fast Layer-3 Handover in Vehicular Networks  

**Bachelor’s Degree – Computer Complexes and Networks (2003–2007)**
""")

# ================= CERTIFICATIONS =================
st.markdown("### 📜 Certifications")

st.markdown("""
- Product Owner – Omdena  
- Data Engineer – Omdena  
- AI Innovation Challenge  
- Text Summarization – Omdena  
- QA Methodologies  
- Python Developer & Machine Learning
""")

# ================= LANGUAGES =================
st.markdown("### 🌍 Languages")

st.markdown("""
- Armenian – Native  
- English – Advanced  
- Russian – Intermediate
""")

# ================= DOWNLOAD CV (CLICKABLE IMAGE) =================
st.markdown("---")
st.markdown("### 📄 Download CV")

# Read PDF
with open("Tsovinar_Babakhanyan_CV.pdf", "rb") as pdf_file:
    pdf_bytes = pdf_file.read()
    pdf_base64 = base64.b64encode(pdf_bytes).decode()

# Read Image
with open("Tsovinar_Babakhanyan_CV.png", "rb") as img_file:
    img_bytes = img_file.read()
    img_base64 = base64.b64encode(img_bytes).decode()

# Clickable Image
st.markdown(
    f"""
    <div style="text-align:center;">
        <a href="data:application/pdf;base64,{pdf_base64}"
           download="Tsovinar_Babakhanyan_CV.pdf">
            <img src="data:image/png;base64,{img_base64}"
                 width="280"
                 style="
                    cursor:pointer;
                    border-radius:14px;
                    box-shadow:0 6px 18px rgba(0,0,0,0.2);
                    transition: transform 0.2s;
                 "
                 onmouseover="this.style.transform='scale(1.05)'"
                 onmouseout="this.style.transform='scale(1)'"
            >
        </a>
        <p style="color:gray; font-size:14px;">
            Click the image to download my CV
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ================= FOOTER =================
st.markdown("---")
st.caption("© 2026 Tsovinar Babakhanyan | Streamlit CV")
