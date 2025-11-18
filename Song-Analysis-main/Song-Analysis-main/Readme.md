🎧 RhythmRanker: AI-Powered Song Popularity Forecast
A comprehensive, end-to-end data science solution focused on deciphering the complex patterns that drive music popularity. The project leverages Machine Learning to accurately forecast a song's success (Spotify Stream Counts) using real-world audio features and market visibility data.

Live Link: [https://song-analysis-data-science-project.streamlit.app/]
📁 Project Structure
.
├── assets/
│   └── images/                # All EDA & feature importance visualizations
├── models/
│   └── random_forest_log_model.pkl   # Final saved model (Random Forest Regressor)
├── notebook/
│   └── song_popularity_analysis.ipynb  # Comprehensive EDA + model development notebook
├── pages/
│   ├── 1_EDA_Insights.py       # In-depth visual analysis
│   ├── 2_Model_Training.py     # Model benchmarking and results
│   ├── 3_Prediction_Tool.py    # Interactive tool for real-time stream prediction
│   └── 4_Project_Summary.py    # Final takeaways for stakeholders
├── utils/
│   └── (optional helper scripts)
├── Home_Page.py               # Landing page and project overview
└── requirements.txt             # Python dependencies list

🧠 Problem Statement & Value Proposition
Challenge: In the competitive streaming landscape, identifying a "hit song" before its release is a multi-million dollar decision. Traditional scouting methods are subjective and slow.

Solution: This project delivers an objective, data-driven tool capable of estimating a song's Spotify stream potential based on key audio metrics (e.g., Energy, Danceability) and critical platform indicators (playlist placement, chart presence).

⚙️ Tech Stack & Methodology
Category,Tools & Libraries,Key Application
Languages,Python (3.x),Core programming for data processing and modeling.
Frameworks,Streamlit,"Built and deployed a fully modular, multi-page interactive dashboard accessible via a web browser."

Modeling,"Random Forest Regressor, XGBoost",Utilized advanced ensemble techniques for high-accuracy regression forecasting.

Libraries,"pandas, numpy, scikit-learn, xgboost, joblib","Data wrangling, ML utilities, high-performance training, and model persistence."

📊 Key Results & Impact📈 Modeling PerformanceApproach: Evaluated multiple models using both raw and log-transformed data to stabilize variance and improve linearity.Best Model: Random Forest Regressor applied to log-transformed stream counts.Accuracy: Achieved a strong predictive performance with an R² score of $\approx 0.79$ (79%).
🎯 Feature ImportanceTop Predictors: Metrics related to Playlist Presence (Spotify, Apple, Deezer) and Chart Visibility proved to be the most critical drivers of future stream counts.Audio Traits: Energy and Danceability were identified as the most impactful intrinsic audio features, helping determine a song's compatibility with popular playlists.
🌐 Dashboard CapabilitiesInteractive EDA: Visualize correlations and distributions directly on the web app.Live Prediction Tool: Allows users to input hypothetical song metrics and receive an instant, forecasted stream count.
💼 Business ImplicationsThis tool provides quantifiable intelligence to maximize music investment:A&R Strategy: Objectively scout high-potential tracks and artists before massive market exposure.Marketing & Scheduling: Optimize release times and platform strategy based on feature trends and seasonality.Playlist Curation: Identify musical traits that guarantee maximum compatibility with high-traffic algorithmic playlists.

🚀 Getting Started (Run Locally)
Install dependencies:

Bash
pip install -r requirements.txt

Run the Streamlit app:
Bash
streamlit run Home_Page.py


✨ Author 
Name : VidhyaShree V
