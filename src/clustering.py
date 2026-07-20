from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import joblib
import os


def perform_clustering(df):
    """
    Perform K-Means clustering on Spotify songs.
    """

    # Features used for clustering
    features = [
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

    X = df[features]

    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # ---------- Elbow Method ----------
    inertia = []

    for k in range(1, 11):
        model = KMeans(n_clusters=k, random_state=42, n_init=10)
        model.fit(X_scaled)
        inertia.append(model.inertia_)

    os.makedirs("outputs/graphs", exist_ok=True)

    plt.figure(figsize=(7,5))
    plt.plot(range(1,11), inertia, marker="o")
    plt.title("Elbow Method")
    plt.xlabel("Number of Clusters")
    plt.ylabel("Inertia")
    plt.savefig("outputs/graphs/elbow_method.png")
    plt.close()

    # ---------- Final KMeans ----------
    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)

    df["Cluster"] = kmeans.fit_predict(X_scaled)

    # ---------- Cluster Visualization ----------
    plt.figure(figsize=(10, 6))

    plt.scatter(
        df["danceability"],
        df["energy"],
        c=df["Cluster"],
        cmap="viridis"
    )

    plt.title("Spotify Song Clusters")
    plt.xlabel("Danceability")
    plt.ylabel("Energy")

    plt.colorbar(label="Cluster")

    plt.tight_layout()
    plt.savefig("outputs/graphs/clusters.png")
    plt.close()

    # Save Model
    os.makedirs("models", exist_ok=True)
    joblib.dump(kmeans, "models/kmeans_model.pkl")

    # Save clustered dataset
    os.makedirs("outputs/results", exist_ok=True)
    df.to_csv("outputs/results/clustered_spotify_songs.csv", index=False)

    print("\n========== CLUSTER COUNTS ==========")
    print(df["Cluster"].value_counts())

    print("\n✅ Clustering completed successfully!")

    print("\n========== CLUSTER FEATURE MEANS ==========\n")

    cluster_summary = df.groupby("Cluster")[[
        "danceability",
        "energy",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo"
    ]].mean()

    print(cluster_summary.round(2))
    
    return df