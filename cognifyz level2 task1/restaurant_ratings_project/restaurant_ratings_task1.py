# File: restaurant_ratings_task1.py
# Level 2 - Task 1: Restaurant Ratings
# Written by a new student for internship project

import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1: Path to the dataset
file_path = r"C:\Users\DELL\Desktop\cognifyz\cognifyz level2 task1\restaurant_ratings_project\data\Dataset.csv"

# Step 2: Load the dataset
try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully.\n")
except Exception as e:
    print("Error reading the file:")
    print(e)
    exit()

# Step 3: Check for required columns
if "Aggregate rating" in data.columns and "Votes" in data.columns:

    # Step 4: Drop missing values
    data = data.dropna(subset=["Aggregate rating", "Votes"])

    # Step 5: Convert data types if needed
    data["Aggregate rating"] = pd.to_numeric(data["Aggregate rating"], errors='coerce')
    data["Votes"] = pd.to_numeric(data["Votes"], errors='coerce')

    # Remove NaNs again after conversion
    data = data.dropna(subset=["Aggregate rating", "Votes"])

    # Step 6: Analyze distribution of ratings
    rating_counts = data["Aggregate rating"].value_counts().sort_index()

    print("Distribution of aggregate ratings:\n")
    print(rating_counts)

    # Step 7: Find the most common rating value
    most_common_rating = rating_counts.idxmax()
    most_common_count = rating_counts.max()

    print("\nMost common rating value is:", most_common_rating)
    print("It occurred", most_common_count, "times.\n")

    # Step 8: Calculate average number of votes
    average_votes = round(data["Votes"].mean(), 2)
    print("Average number of votes received by restaurants:", average_votes)

    # Step 9: Save result to CSV
    output_path = r"C:\Users\DELL\Desktop\cognifyz\cognifyz level2 task1\restaurant_ratings_project\output\restaurant_ratings_result.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    result_df = pd.DataFrame({
        "Aggregate Rating": rating_counts.index,
        "Restaurant Count": rating_counts.values
    })

    result_df["Most Common"] = result_df["Aggregate Rating"] == most_common_rating
    result_df.to_csv(output_path, index=False)
    print("\nResults saved to:", output_path)

    # Step 10: Plot histogram
    plt.figure(figsize=(8, 5))
    plt.bar(rating_counts.index.astype(str), rating_counts.values, color='green')
    plt.xlabel("Aggregate Rating")
    plt.ylabel("Number of Restaurants")
    plt.title("Distribution of Aggregate Ratings")
    plt.tight_layout()
    plt.show()

else:
    print("Required columns not found in dataset.")
