import pandas as pd
file_path = r"C:\Users\DELL\Desktop\cognifyz\cognifyz level 1task1\TopCuisines_Project\data\Dataset.csv"
try:
    data = pd.read_csv(file_path)
    print(" Data file opened successfully!\n")
except Exception as error:
    print(" Something went wrong while opening the file:")
    print(error)
    exit()
if "Cuisines" in data.columns:

    data = data.dropna(subset=["Cuisines"])

    cuisine_names = []
    for each in data["Cuisines"]:
        each_split = str(each).split(",")
        for one in each_split:
            cuisine_names.append(one.strip())  


    counts = {}
    for c in cuisine_names:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    
    sorted_cuisines = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    top_three = sorted_cuisines[:3]

    total = len(data)
    result = []

    print(" These are the top 3 cuisines served by most restaurants:\n")
    for item in top_three:
        name = item[0]
        num = item[1]
        percent = round((num / total) * 100, 2)
        result.append([name, num, percent])
        print(f"- {name}: {num} times ({percent}%)")

   
    output_path = r"C:\Users\DELL\Desktop\cognifyz\cognifyz level 1task1\TopCuisines_Project\output\top_cuisines_result.csv"
    df_result = pd.DataFrame(result, columns=["Cuisine Name", "How Many Times", "Percentage"])
    df_result.to_csv(output_path, index=False)

    print("\n The result is also saved to:")
    print(output_path)

else:
    print(" The column named 'Cuisines' is not in the file. Please check the CSV.")
