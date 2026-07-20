import streamlit as st
import pandas as pd
from src.recommendation import recommend_songs

st.set_page_config(
    page_title="Spotify Music Recommendation",
    page_icon="🎵",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background-color:#121212;
    color:white;
}
/* Sidebar background */

section[data-testid="stSidebar"]{
    background:#000000 !important;
}
            
/* All sidebar text */

section[data-testid="stSidebar"] *{
    color:white !important;
}

h1,h2,h3,h4,h5,h6{
    color:white;
}

[data-testid="stTextInput"] input{
    background-color:#2b2b2b;
    color:white;
    border-radius:12px;
}

/* ---------- Input Label ---------- */

label{
    color:white !important;
    font-size:18px !important;
    font-weight:bold !important;
}

[data-testid="stWidgetLabel"]{
    color:white !important;
}

div[data-testid="stTextInput"] label p{
    color:white !important;
    font-size:18px !important;
    font-weight:bold !important;
}

[data-testid="stTextInput"] input::placeholder{
    color:#b3b3b3 !important;
}

.stButton>button{
    width:100%;
    margin:0;
    background-color:#1DB954;
    color:white;
    border-radius:12px;
    height:55px;
    font-size:18px;
    font-weight:bold;
    border:none;
}

.stButton>button:hover{
    background-color:#18a64d;
}

.song-card{
    display:flex;
    align-items:center;
    gap:25px;

    background:#1b1b1b;

    padding:18px;

    margin:18px 0;

    border-radius:20px;

    border-left:5px solid #1DB954;

    transition:.3s;

    box-shadow:0 8px 22px rgba(0,0,0,.45);
}
.song-card:hover{
    transform:translateY(-4px);
    transition:0.3s;
    box-shadow:0 0 25px rgba(29,185,84,0.35);
}           
.album-cover{
    width:120px;
    height:120px;
    border-radius:18px;
    object-fit:cover;
}

.song-info{
    flex:1;
}

.song-card h3{
    color:white;
    font-size:36px;
    margin-bottom:12px;
}

.song-card p{
    color:#d6d6d6;
    font-size:22px;
    margin:12px 0;
}
.genre-badge{
    display:inline-block;
    background:#1DB954;
    color:white;
    padding:8px 16px;
    border-radius:25px;
    font-weight:bold;
    font-size:14px;
    letter-spacing:1px;
}

/* Metric Numbers */

[data-testid="stMetricValue"]{
    color:#FFFFFF !important;
    font-size:42px !important;
    font-weight:700 !important;
}

/* Metric Labels */

[data-testid="stMetricLabel"]{
    color:#B3B3B3 !important;
    font-size:18px !important;
}



</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style="font-size:54px;margin-bottom:0;">
<span style="color:#1DB954;">🎵</span>
<span style="color:white;">Spotify Music </span><span style="color:#1DB954;">Recommendation</span>
</h1>

<h3 style="color:#B3B3B3;margin-top:10px;">
Discover Similar Songs using Machine Learning
</h3>

<hr>
""", unsafe_allow_html=True)

st.success("🎧 Search your favourite song and discover similar music instantly.")

# Load dataset once
@st.cache_data
def load_data():
    return pd.read_csv("data/spotify_songs.csv")

df = load_data()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎵 Total Songs", f"{len(df):,}")

with col2:
    st.metric("🎼 Genres", df["playlist_genre"].nunique())

with col3:
    st.metric("🤖 AI Model", "Cosine")
    
with st.sidebar:

    st.markdown("""
    <div style="display:flex;align-items:center;gap:14px;">

    <img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Spotify_icon.svg"
    width="55">

    <h2 style="margin:0;font-size:28px;font-weight:700;">
    <span style="color:white;">Spotify</span>
    <span style="color:#1DB954;"> AI</span>
    </h2>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🏠 Music Recommendation")
    st.markdown("### 🤖 Machine Learning")
    st.markdown("### 📊 Dataset: Spotify Songs")

    st.markdown("---")

    st.markdown("## 📈 Statistics")

    st.markdown(f"""
    <div style="
    background:#161b22;
    padding:18px;
    border-radius:15px;
    margin-bottom:15px;
    border:1px solid #2b2b2b;">

    <h4 style="margin:0;color:#b3b3b3;">🎵 Total Songs</h4>

    <h2 style="margin-top:10px;color:white;">
    {len(df):,}
    </h2>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
    background:#161b22;
    padding:18px;
    border-radius:15px;
    border:1px solid #2b2b2b;">

    <h4 style="margin:0;color:#b3b3b3;">🎼 Total Genres</h4>

    <h2 style="margin-top:10px;color:white;">
    {df["playlist_genre"].nunique()}
    </h2>

    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="
    margin-top:25px;
    padding:20px;
    border-radius:15px;
    background:#0d1117;
    border:1px solid #1DB954;">

    <h4 style="color:#b3b3b3;margin-bottom:15px;">
    Developed using
    </h4>

    <p style="color:white;font-size:17px;line-height:2;">
    Python<br>
    Streamlit<br>
    Scikit-Learn
    </p>

    <div style="font-size:26px;">
    💚
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
song = st.text_input(
    "🎵 Song Name",
    placeholder="Example: Believer"
)

if st.button("🎧 Recommend Songs", use_container_width=True):

    if song.strip() == "":
        st.warning("Please enter a song name.")

    else:

        recommendations = recommend_songs(df, song)

        if recommendations is None:
            st.error("Song not found!")

        else:

            st.markdown("""
            <h2 style="color:#1DB954;">
            ✨ Recommended Songs
            </h2>
            """, unsafe_allow_html=True)
            for rec in recommendations:

                    st.markdown(f"""
                    <div style="
                    display:flex;
                    align-items:center;
                    gap:22px;
                    background:linear-gradient(135deg,#1a1a1a,#252525);
                    padding:20px;
                    border-radius:20px;
                    margin-bottom:28px;
                    border-left:6px solid #1DB954;
                    box-shadow:0 8px 22px rgba(0,0,0,.45);
                    position:relative;
                    ">

                    <div style="
                    position:absolute;
                    top:18px;
                    right:18px;
                    font-size:24px;
                    color:#1DB954;
                    ">
                    💚
                    </div>

                    <img src="https://cdn-icons-png.flaticon.com/512/3844/3844724.png"
                    style="
                    width:90px;
                    height:90px;
                    border-radius:16px;
                    flex-shrink:0;
                    ">

                    <div style="
                    display:flex;
                    flex-direction:column;
                    justify-content:center;
                    ">

                    <h2 style="
                    margin:0;
                    color:white;
                    font-size:32px;
                    font-weight:700;
                    letter-spacing:.3px;
                    ">
                    {rec['Song']}
                    </h2>

                    <p style="margin:8px 0;font-size:18px;color:#D8D8D8;">
                    <span style="color:#1DB954;font-weight:bold;">👤 Artist:</span>
                    <span style="color:white;font-weight:500;">
                    {rec['Artist']}
                    </span>
                    </p>

                    <p style="margin:5px 0;font-size:16px;color:#D8D8D8;">
                    <span style="color:#1DB954;font-weight:bold;">💿 Album:</span>
                    <span style="color:white;">
                    {rec['Album']}
                    </span>
                    </p>

                    <p style="margin:5px 0;font-size:16px;color:#D8D8D8;">
                    <span style="color:#1DB954;font-weight:bold;">📅 Released:</span>
                    <span style="color:white;">
                    {rec['Year']}
                    </span>
                    </p>

                    <p style="margin:5px 0;font-size:16px;color:#D8D8D8;">
                    <span style="color:#1DB954;font-weight:bold;">⏱ Duration:</span>
                    <span style="color:white;">
                    {rec['Duration']}
                    </span>
                    </p>

                    <div style="
                    display:inline-flex;
                    align-items:center;
                    justify-content:center;
                    background:#1DB954;
                    color:white;
                    padding:8px 18px;
                    border-radius:999px;
                    font-size:14px;
                    font-weight:700;
                    margin-top:10px;
                    width:max-content;
                    letter-spacing:.6px;
                    ">
                    {rec['Genre'].upper()}
                    </div>

                    <a href="https://open.spotify.com/search/{rec['Song']} {rec['Artist']}"
                    target="_blank"
                    style="
                    display:inline-block;
                    margin-top:15px;
                    padding:10px 18px;
                    background:#1DB954;
                    color:white;
                    text-decoration:none;
                    border-radius:30px;
                    font-weight:bold;
                    font-size:15px;
                    width:max-content;
                    ">
                    ▶ Listen on Spotify
                    </a>

                    </div>

                    </div>
                    """, unsafe_allow_html=True)