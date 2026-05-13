import pandas as pd
import os

# Define paths
diary_path = 'Dataset/diary.csv'
reviews_path = 'Dataset/reviews.csv'
output_path = 'Dataset/main.csv'

# Check if files exist
if not os.path.exists(diary_path) or not os.path.exists(reviews_path):
    print(f"Error: Required files not found in Dataset/ directory.")
else:
    print(f"Loading {diary_path} and {reviews_path}...")
    # Load the data
    diary_df = pd.read_csv(diary_path)
    reviews_df = pd.read_csv(reviews_path)

    # Select only necessary columns from reviews to avoid duplicates
    # We use 'Letterboxd URI' as the key to join uniquely for each log entry
    reviews_subset = reviews_df[['Letterboxd URI', 'Review']]

    # Merge diary entries with reviews
    # Left join ensures we keep all diary entries, even those without reviews
    print("Merging data...")
    main_df = pd.merge(diary_df, reviews_subset, on='Letterboxd URI', how='left')

    # Save the result
    main_df.to_csv(output_path, index=False)
    print(f"Successfully created {output_path} with {len(main_df)} rows.")
