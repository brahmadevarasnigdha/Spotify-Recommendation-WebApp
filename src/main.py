from preprocessing import load_data, explore_data, clean_data
from visualization import create_visualizations
from clustering import perform_clustering
from recommendation import recommend_songs

# Dataset path
file_path = "data/spotify_songs.csv"

# Load data
df = load_data(file_path)

# Explore data
explore_data(df)

# Clean data
df = clean_data(df)

# Create graphs
create_visualizations(df)

# Perform clustering
df = perform_clustering(df)

song = input("\nEnter a song name: ")

recommend_songs(df, song)