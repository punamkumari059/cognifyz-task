
import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\DELL\Desktop\cognifyz\cognifyz level2 task3\geographic_analysis_project\data\Dataset.csv"

try:
    data = pd.read_csv(file_path)
    print("File loaded successfully.\n")
except Exception as e:
    print("Error loading file:")
    print(e)
    exit()

# Step 3: Check if Latitude and Longitude exist
if "Latitude" in data.columns and "Longitude" in data.columns:

    # Step 4: Remove rows with missing coordinates
    data = data.dropna(subset=["Latitude", "Longitude"])

    # Step 5: Plot locations on scatter plot
    print("Now displaying map with restaurant locations...\n")

    plt.figure(figsize=(8, 6))
    plt.scatter(data["Longitude"], data["Latitude"], alpha=0.4, s=10, c='red')
    plt.title("Restaurant Locations (Longitude vs Latitude)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

else:
    print("Columns 'Latitude' and/or 'Longitude' are missing in the dataset.")
