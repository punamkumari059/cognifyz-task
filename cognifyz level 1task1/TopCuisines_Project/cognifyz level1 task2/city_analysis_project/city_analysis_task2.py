

import pandas as pd
import os

file_path = r"C:\Users\DELL\Desktop\cognifyz\cognifyz level1 task2\city_analysis_project\data\Dataset.csv"

try:
    data = pd.read_csv(file_path)
    print("Data loaded successfully!\n")
except Exception as e:
    print("There was an error while loading the data file:")
    print(e)
    exit()

if "City" in data.columns and "Aggregate rating" in data.columns:

    data = data.dropna(subset=["City", "Aggregate rating"])

    city_counts = data["City"].value_counts()
    top_city = city_counts.idxmax()
    top_count = city_counts.max()
    print("City with the highest number of restaurants:")
    print(top_city, "-", top_count, "restaurants\n")
    avg_ratings = data.groupby("City")["Aggregate rating"].mean()
    print("Average rating per city:\n")
    print(avg_ratings.round(2).sort_values(ascending=False))
    best_city = avg_ratings.idxmax()
    best_rating = round(avg_ratings.max(), 2)
    print("\nCity with the highest average rating:")
    print(best_city, "-", best_rating)

    output_path = r"C:\Users\DELL\Desktop\cognifyz\cognifyz level1 task2\city_analysis_project\output\city_analysis_result.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    result_df = pd.DataFrame({
        "City": avg_ratings.index,
        "Average Rating": avg_ratings.values
    })

    result_df.to_csv(output_path, index=False)
    print("\nResults saved to:")
    print(output_path)

else:
    print("The dataset is missing required columns.")
