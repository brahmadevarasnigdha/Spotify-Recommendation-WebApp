from sklearn.metrics.pairwise import cosine_similarity

def recommend_songs(df, song_name):
    """
    Recommend songs similar to the given song.
    Returns a list of recommended songs.
    """

    song_name = song_name.strip().lower()

    df["track_name_lower"] = df["track_name"].str.lower()

    if song_name not in df["track_name_lower"].values:
        return None

    numeric_features = [
        "danceability",
        "energy",
        "loudness",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo"
    ]

    index = df[df["track_name_lower"] == song_name].index[0]

    # Calculate similarity ONLY for the selected song
    similarity = cosine_similarity(
        [df.loc[index, numeric_features]],
        df[numeric_features]
    )[0]

    scores = list(enumerate(similarity))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    recommended = {song_name}

    for i, score in scores[1:]:

        row = df.iloc[i]

        if row["track_name"] in recommended:
            continue

        recommended.add(row["track_name"])

        minutes = int(row["duration_ms"] // 60000)
        seconds = int((row["duration_ms"] % 60000) // 1000)

        recommendations.append({
        "Song": row["track_name"],
        "Artist": row["track_artist"],
        "Genre": row["playlist_genre"],
        "Album": row["track_album_name"],
        "Year": str(row["track_album_release_date"])[:4],
        "Duration": f"{minutes}:{seconds:02d}",
        "Match": round(score * 100, 1)
    })

        if len(recommendations) == 5:
            break

    return recommendations