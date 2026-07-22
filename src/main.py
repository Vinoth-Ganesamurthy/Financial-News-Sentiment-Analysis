from news_loader import load_dataset


def main() -> None:
    df = load_dataset("data/raw/all-data.csv")

    print(df.head())
    print(f"\nTotal records: {len(df)}")


if __name__ == "__main__":
    main()