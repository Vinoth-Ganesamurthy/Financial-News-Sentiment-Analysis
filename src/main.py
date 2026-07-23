from data.news_loader import load_dataset
from data.data_validator import validate_dataset
from preprocessing.text_preprocessor import preprocess_dataset


def main() -> None:
    # Load the dataset
    df = load_dataset("data/raw/all-data.csv")

    # Validate the dataset
    validate_dataset(df)

    # Preprocess the dataset
    processed_df = preprocess_dataset(df)

    # Display the first 5 cleaned records
    print("\nFirst 5 cleaned headlines:\n")
    print(processed_df.head())


if __name__ == "__main__":
    main()