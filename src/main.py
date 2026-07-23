from data.news_loader import load_dataset
from data.data_validator import validate_dataset
from preprocessing.text_preprocessor import preprocess_dataset
from data.duplicate_handler import (
    inspect_duplicates,
    remove_duplicates,
)
from data.data_saver import save_dataset


def main() -> None:
    # Load dataset
    df = load_dataset("data/raw/all-data.csv")

    # Validate dataset
    validate_dataset(df)

    # Preprocess dataset
    processed_df = preprocess_dataset(df)

    # Inspect duplicates
    inspect_duplicates(processed_df)

    # Remove duplicates
    cleaned_df = remove_duplicates(processed_df)

    save_dataset(
    cleaned_df,
    "data/processed/financial_news_cleaned.csv",
)
    
    # Display cleaned dataset
    print("\nFirst 5 cleaned headlines:\n")
    print(cleaned_df.head())


if __name__ == "__main__":
    main()