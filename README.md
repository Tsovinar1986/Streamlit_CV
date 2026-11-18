# Tsovinar Babakhanyan – CV website

My CV as a web page, hosted for free on Streamlit Community Cloud (https, no custom domain needed).

- `index.html`: the page (projects, experience, skills, certifications), live at https://tsovinar1986.github.io/Streamlit_CV/
- `site/photo.jpg`: portrait embedded in the page
- `cv_str.py`: Streamlit app that serves the page

## Run locally
```bash
pip install -r requirements.txt
streamlit run cv_str.py
```

## Deploy
On https://share.streamlit.io choose this repo, branch `main`, main file `cv_str.py`.
Every push to `main` redeploys.
