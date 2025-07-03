# File: online_delivery_task4.py
# Level 1 - Task 4: Online Delivery
# Code written by a beginner student

import pandas as pd
import os

# Step 1: File path of the dataset
file_path = r"C:\Users\DELL\Desktop\cognifyz\cognifyz level1 task4\online_delivery_project\data\Dataset.csv"

# Step 2: Load the data
try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully!\n")
except Exception as e:
    print("Error loading file:")
    print(e)
    exit()

# Step 3: Check required columns
if "Has Online delivery" in data.columns and "Aggregate rating" in data.columns:

    # Step 4: Remove missing values
    data = data.dropna(subset=["Has Online delivery", "Aggregate rating"])

    # Step 5: Count how many restaurants offer and don't offer online delivery
    delivery_counts = data["Has Online delivery"].value_counts()
    total_restaurants = delivery_counts.sum()

    # Step 6: Calculate percentage
    yes_count = delivery_counts.get("Yes", 0)
    no_count = delivery_counts.get("No", 0)

    yes_percent = round((yes_count / total_restaurants) * 100, 2)
    no_percent = round((no_count / total_restaurants) * 100, 2)

    print("Percentage of restaurants with online delivery:")
    print("Yes:", yes_percent, "%")
    print("No:", no_percent, "%\n")

    # Step 7: Compare average ratings
    avg_with_delivery = data[data["Has Online delivery"] == "Yes"]["Aggregate rating"].mean()
    avg_without_delivery = data[data["Has Online delivery"] == "No"]["Aggregate rating"].mean()

    avg_with_delivery = round(avg_with_delivery, 2)
    avg_without_delivery = round(avg_without_delivery, 2)

    print("Average rating of restaurants WITH online delivery:", avg_with_delivery)
    print("Average rating of restaurants WITHOUT online delivery:", avg_without_delivery)

    # Step 8: Save output to CSV
    output_path = r"C:\Users\DELL\Desktop\cognifyz\cognifyz level1 task4\online_delivery_project\output\online_delivery_result.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    result_df = pd.DataFrame({
        "Online Delivery": ["Yes", "No"],
        "Restaurant Count": [yes_count, no_count],
        "Percentage": [yes_percent, no_percent],
        "Average Rating": [avg_with_delivery, avg_without_delivery]
    })

    result_df.to_csv(output_path, index=False)
    print("\nResult saved to:", output_path)

else:
    print("Required columns not found in the dataset.")
