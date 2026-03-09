# Wood Moisture Content Calculator
# You can either type in your values manually or upload a CSV file

import pandas as pd

print("WOOD MOISTURE CONTENT CALCULATOR")

print("How do you want to enter your data?")
print("1. Type it in manually")
print("2. Upload a CSV file")

choice = input("Enter 1 or 2: ")


# Formula: Moisture Content = ((Wet Weight - Dry Weight) / Dry Weight) x 100
def calculate_moisture(wet, dry):
    moisture = ((wet - dry) / dry) * 100
    return round(moisture, 2)

def classify(mc):
    if mc < 12:
        return "Dry - suitable for use"
    elif mc <= 19:
        return "Moderate - suitable for construction"
    else:
        return "Too wet - needs more drying"

# OPTION 1: Manual input
if choice == "1":
    print("\nEnter your sample details:")
    sample_name = input("Sample name (e.g. Iroko): ")
    wet_weight = float(input("Wet weight (grams): "))
    dry_weight = float(input("Dry weight (grams): "))

    mc = calculate_moisture(wet_weight, dry_weight)

    print("\nRESULT:")
    print("Sample:", sample_name)
    print("Wet Weight:", wet_weight, "g")
    print("Dry Weight:", dry_weight, "g")
    print("Moisture Content:", mc, "%")
    print("Status:", classify(mc))



# OPTION 2: CSV file
elif choice == "2":
    from google.colab import files

    print("\nUpload your CSV file now...")
    uploaded = files.upload()

    # Read the uploaded file
    filename = list(uploaded.keys())[0]
    df = pd.read_csv(filename)

    print("\nRESULTS FROM CSV:")
    # Apply the calculation and classification to each row
    df['Moisture Content (%)'] = df.apply(lambda row: calculate_moisture(row['Wet Weight (g)'], row['Dry Weight (g)']), axis=1)
    df['Status'] = df['Moisture Content (%)'].apply(classify)

    # Print results for each sample
    for index, row in df.iterrows():
        print(f"\nSample: {row['Sample']}")
        print(f"Wet Weight: {row['Wet Weight (g)']} g")
        print(f"Dry Weight: {row['Dry Weight (g)']} g")
        print(f"Moisture Content: {row['Moisture Content (%)']}%")
        print(f"Status: {row['Status']}")
