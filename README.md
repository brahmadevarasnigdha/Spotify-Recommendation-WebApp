# 🎵 Spotify Music Recommendation Web App

A Spotify-inspired Music Recommendation Web Application built using Python, Streamlit, and Machine Learning. The system recommends similar songs using Cosine Similarity based on audio features and provides an interactive, modern user interface for music discovery.

## 🚀 Features

- 🎵 Search songs by name
- 🤖 Machine Learning recommendation engine
- 🎯 Cosine Similarity-based recommendations
- 💿 Album information
- 👤 Artist details
- 📅 Release year
- ⏱ Song duration
- 🎧 Direct Spotify search button
- 🌙 Modern Spotify-inspired UI

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- NumPy
- HTML & CSS

## 📂 Dataset

Spotify Songs Dataset containing:
- Track Name
- Artist
- Album
- Genre
- Release Date
- Duration
- Audio Features



## ▶️ Run the Project

```bash
pip install -r requirements.txt

streamlit run app.py
```

## 📖 Machine Learning

The recommendation system uses **Cosine Similarity** on Spotify audio features such as:

- Danceability
- Energy
- Tempo
- Valence
- Loudness
- Acousticness
- Instrumentalness
- Speechiness
- Liveness

to recommend songs similar to the selected track.

## 👨‍💻 Developer

Snigdha Brahmadevara