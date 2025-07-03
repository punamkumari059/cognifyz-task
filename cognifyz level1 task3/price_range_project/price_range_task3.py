import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = r"C:\Users\DELL\Desktop\cognifyz\cognifyz level1 task3\price_range_project\data\Dataset.csv"

try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully.\n")
except Exception as error:
    print("Error loading dataset:")
    print(error)
    exit()
if "Price range" in data.columns:

    data = data.dropna(subset=["Price range"])

    price_counts = data["Price range"].value_counts().sort_index()

    
    total = price_counts.sum()

    percentages = (price_counts / total) * 100

    result_df = pd.DataFrame({
        "Price Range": price_counts.index,
        "Restaurant Count": price_counts.values,
        "Percentage (%)": percentages.round(2)
    })

    print("Price Range Distribution:\n")
    print(result_df)

    output_path = r"C:\Users\DELL\Desktop\cognifyz\cognifyz level1 task3\price_range_project\output\price_range_result.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    result_df.to_csv(output_path, index=False)
    print("\nData saved to:", output_path)

    plt.figure(figsize=(7, 5))
    plt.bar(result_df["Price Range"].astype(str), result_df["Restaurant Count"], color='skyblue')
    plt.xlabel("Price Range")
    plt.ylabel("Number of Restaurants")
    plt.title("Distribution of Price Ranges")
    plt.tight_layout()

    plt.show()

else:
    print("Column 'Price range' not found in the dataset.")
