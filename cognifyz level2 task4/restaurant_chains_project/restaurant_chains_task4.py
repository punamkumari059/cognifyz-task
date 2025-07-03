import pandas as pd
file_path = r"C:\Users\DELL\Desktop\cognifyz\cognifyz level2 task4\restaurant_chains_project\data\Dataset.csv"

try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully.\n")
except Exception as e:
    print("Error while loading the file:")
    print(e)
    exit()

if "Restaurant Name" in data.columns and "Aggregate rating" in data.columns and "Votes" in data.columns:

    restaurant_counts = data["Restaurant Name"].value_counts()
    
    chains = restaurant_counts[restaurant_counts > 1]
    
    if len(chains) == 0:
        print("No restaurant chains found in the dataset.")
    else:
        print("Restaurant chains found:\n")
        print(chains.head(10))  # Show top 10 chains
        
        # Step 6: Analyze average rating and votes for each chain
        grouped = data.groupby("Restaurant Name").agg({
            "Aggregate rating": "mean",
            "Votes": "mean",
            "Restaurant Name": "count"
        })

        grouped = grouped[grouped["Restaurant Name"] > 1]

        grouped = grouped.rename(columns={
            "Aggregate rating": "Average Rating",
            "Votes": "Average Votes",
            "Restaurant Name": "Location Count"
        })

        # Round values
        grouped["Average Rating"] = grouped["Average Rating"].round(2)
        grouped["Average Votes"] = grouped["Average Votes"].round(1)

        
        print("\nTop 10 restaurant chains based on rating:\n")
        print(grouped.sort_values(by="Average Rating", ascending=False).head(10))

        
        print("\nTop 10 restaurant chains based on popularity (votes):\n")
        print(grouped.sort_values(by="Average Votes", ascending=False).head(10))

else:
    print("Required columns 'Restaurant Name', 'Aggregate rating', or 'Votes' are missing.")
