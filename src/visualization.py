import matplotlib.pyplot as plt
import seaborn as sns
import os


def create_visualizations(df):
    """
    Create and save basic visualizations.
    """

    os.makedirs("outputs/graphs", exist_ok=True)

    # 1. Genre Count Plot
    plt.figure(figsize=(8,5))
    sns.countplot(data=df, x="playlist_genre")
    plt.title("Songs by Genre")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/graphs/genre_count.png")
    plt.close()

    # 2. Popularity Distribution
    plt.figure(figsize=(8,5))
    plt.hist(df["track_popularity"], bins=20)
    plt.title("Track Popularity Distribution")
    plt.xlabel("Popularity")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("outputs/graphs/popularity_histogram.png")
    plt.close()

    # 3. Correlation Matrix
    plt.figure(figsize=(12,8))

    numeric_df = df.select_dtypes(include=["number"])

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.savefig("outputs/graphs/correlation_matrix.png")
    plt.close()
    print("\n✅ Graphs saved successfully!")