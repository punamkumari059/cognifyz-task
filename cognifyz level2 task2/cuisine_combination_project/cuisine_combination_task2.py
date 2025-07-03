import pandas as pd

file_path = r"C:\Users\DELL\Desktop\cognifyz\cognifyz level2 task2\cuisine_combination_project\data\Dataset.csv"

try:
    data = pd.read_csv(file_path)
    print("File loaded successfully.\n")
except Exception as e:
    print("Error loading file:")
    print(e)
    exit()

if "Cuisines" in data.columns and "Aggregate rating" in data.columns:

    data = data.dropna(subset=["Cuisines", "Aggregate rating"])

    def clean_combo(text):
        parts = str(text).split(",")
        parts = [p.strip() for p in parts]
        parts.sort()
        return ", ".join(parts)

    data["Cuisine Combo"] = data["Cuisines"].apply(clean_combo)

    combo_counts = data["Cuisine Combo"].value_counts()
    top_10_combos = combo_counts.head(10)

    print("Top 10 Cuisine Combinations:\n")
    print(top_10_combos)

    print("\nAverage Rating for Top 10 Cuisine Combinations:\n")
    for combo in top_10_combos.index:
        avg_rating = data[data["Cuisine Combo"] == combo]["Aggregate rating"].mean()
        print(f"{combo} --> Average Rating: {round(avg_rating, 2)}")

else:
    print("Required columns are missing in the dataset.")
