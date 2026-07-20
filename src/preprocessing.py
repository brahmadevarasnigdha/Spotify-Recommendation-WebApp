import pandas as pd


def load_data(file_path):
    """
    Load the Spotify dataset.
    """
    df = pd.read_csv(file_path)
    return df


def explore_data(df):
    """
    Display basic information about the dataset.
    """
    print("\n========== FIRST 5 ROWS ==========")
    print(df.head())

    print("\n========== DATASET SHAPE ==========")
    print(df.shape)

    print("\n========== COLUMN NAMES ==========")
    print(df.columns)

    print("\n========== DATASET INFO ==========")
    df.info()

    print("\n========== STATISTICAL SUMMARY ==========")
    print(df.describe())

def clean_data(df):
    """
    Clean the dataset by handling missing values and duplicates.
    """

    print("\n========== MISSING VALUES ==========")
    print(df.isnull().sum())

    print("\n========== DUPLICATE ROWS ==========")
    print(df.duplicated().sum())

    # Remove missing values
    df = df.dropna()

    # Remove duplicate rows
    df = df.drop_duplicates()

    print("\n========== AFTER CLEANING ==========")
    print(df.shape)

    return df