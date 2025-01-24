import streamlit as st

# --- SHARED ON ALL PAGES ---
st.sidebar.caption("Made by Team 8 - RightBrothers, Dept of AIML, PESITM, Shivamogga")

# --- PAGE SETUP ---
# --- PAGE SETUP ---
project_1_page = st.Page(
    "views/judgmentPred.py",
    title="Judgment Predictor",
    icon=":material/online_prediction:",
)
project_2_page = st.Page(
    "views/docGen.py",
    title="Legal Doc Generator",
    icon=":material/description:",
)
# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "AI Legal Assistant": [about_page],
        "Tools": [project_1_page, project_2_page],
    }
)

# --- RUN NAVIGATION ---
pg.run()
