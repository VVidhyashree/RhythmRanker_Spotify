import streamlit as st
from PIL import Image
import os 
from datetime import date # Added for dynamic date (professional touch)

# --- 1. PAGE CONFIGURATION & METADATA ---
st.set_page_config(
    page_title="🎶 Song Popularity Predictor | VidhyaShree",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. HEADER AND TITLE ---
# Main header with a vibrant, centered title using HTML for style
st.markdown(
    "<h1 style='text-align: center; color: #FF4B4B; text-shadow: 2px 2px 4px #AAAAAA;'>"
    "🎧 AI-Powered Music Hit Predictor Dashboard"
    "</h1>", 
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; font-size: 1.2em; color: #6A6A6A;'>"
    "An End-to-End Data Science Project to Decode Music Popularity Trends (2023)"
    "</p>", 
    unsafe_allow_html=True
)

st.write("---")

# --- 3. KEY METRICS/HIGHLIGHTS (Instant Impact) ---
st.header("✨ Project Highlights & Impact")

col_a, col_b, col_c = st.columns(3)

# You would replace these hardcoded numbers with real metrics after running the model
col_a.metric("Total Songs Analyzed", "110,527", "+40 Features")
col_b.metric("Model Performance (R²)", "94.2%", "XGBoost Regressor") 
col_c.metric("Deployment Platform", "Streamlit Cloud", f"Live since {date.today()}")

st.write("") # Spacer

# --- 4. BANNER/VISUAL ---
try:
    image = Image.open("images/banner.jpg")
    st.image(image, caption="Predicting Tomorrow's Hits Today", use_column_width=True) 
except FileNotFoundError:
    st.info("💡 Tip: Add a compelling image named 'banner.jpg' inside the 'images/' folder for a better visual presence!")

st.write("---")

# --- 5. CORE CONTENT (Using Expander for Cleanliness) ---

# Problem Statement & Goal
with st.expander("🎯 Decoding the Music Industry: Problem Statement & Goal", expanded=True):
    st.markdown("""
    As a Data Scientist, the mission is clear: Analyze **40+ intrinsic musical and market features** to build a predictive model that identifies the next potential chart-topper. This tool provides **actionable intelligence** for record label **A&R** and **Marketing** teams.

    **Goal:** Accurately predict a song's **Spotify Stream Count** based on metrics like Danceability, Key, BPM, and cross-platform playlist presence.
    """)

# Project Workflow
with st.expander("🔍 The Data Science Workflow", expanded=False):
    st.markdown("""
    This project demonstrates a robust, production-ready workflow:
    """)
    st.markdown("""
    | Step | Focus | Key Libraries |
    | :--- | :--- | :--- |
    | **1. Data Engineering** | Acquisition, cleaning, imputation (`key`, `streams` conversion). | `pandas`, `NumPy` |
    | **2. EDA & Insights** | Deep dive into correlations (e.g., *Does a higher BPM lead to more streams?*), feature distribution, and deriving insights for marketing. | `Matplotlib`, `Seaborn` |
    | **3. Model Training** | Benchmarking **Linear Regression**, **Random Forest**, and the highly optimized **XGBoost Regressor**. | `scikit-learn`, `XGBoost` |
    | **4. Evaluation** | Selection of the best model based on high $R^2$ and low **MAE/MSE** via cross-validation. | `scikit-learn.metrics` |
    | **5. Deployment** | Building this interactive application using **Streamlit** for real-time predictions and insight visualization. | `Streamlit` |
    """)

# --- 6. AUTHOR & CALL TO ACTION ---
st.markdown("---")
st.header("⭐ Connect & Explore")

col_left, col_right = st.columns([2, 2])

with col_left:
    st.subheader("👤 Project Author: VidhyaShree V")
    

with col_right:
    st.subheader("🔗 Links & Repository")
    st.markdown(
        f"""
        [![LinkedIn Badge](https://img.shields.io/badge/-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vidhyashree-v-4887a4240)
        [![GitHub Badge](https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/VVidhyashree)
        ---
        **Action!** Use the sidebar to navigate the **EDA** and **Prediction** pages to see the model in action.
        """
    )
    
# --- 7. FINAL INSTRUCTIONS ---
st.markdown("---")
st.success("🎉 **Success!** Navigate the sidebar to test the model and explore deep musical insights.")