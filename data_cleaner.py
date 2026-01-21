# Python Data Cleaner & Reporter – Great for freelance gigs!
# Cleans duplicates, missing values, adds calculations, saves cleaned file + summary

import pandas as pd

# Configuration – easy to change for different files
input_file = "sample_input.csv"      # Or change to your .xlsx file
output_file = "cleaned_output.csv"   # Or "cleaned.xlsx"
fill_strategy = 0                    # Options: 0, "mean", "median", or custom value

print(f"Processing file: {input_file}")

try:
    # Load data
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    elif input_file.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(input_file)
    else:
        raise ValueError("File must be .csv or .xlsx")

    print("\nOriginal Data Preview:")
    print(df.head())
    print(f"\nOriginal shape: {df.shape} rows/columns")

    # Clean steps
    original_rows = df.shape[0]
    df = df.drop_duplicates()
    print(f"After removing duplicates: {df.shape[0]} rows (removed {original_rows - df.shape[0]})")

    # Fill missing
    if fill_strategy == "mean":
        df = df.fillna(df.mean(numeric_only=True))
    elif fill_strategy == "median":
        df = df.fillna(df.median(numeric_only=True))
    else:
        df = df.fillna(fill_strategy)

    # Add example calculation (customize based on columns)
    if 'Salary' in df.columns:
        df['Bonus_10pct'] = df['Salary'] * 0.10
        print("Added 'Bonus_10pct' column (10% of Salary)")

    # Summary report
    summary = {
        "Total Rows After Clean": df.shape[0],
        "Columns": df.shape[1],
        "Remaining Missing Values": df.isnull().sum().sum(),
        "Average Salary": df.get('Salary', 0).mean(),
        "Total Salary": df.get('Salary', 0).sum(),
        "Total Bonus": df.get('Bonus_10pct', 0).sum()
    }

    print("\n=== Summary Report ===")
    for k, v in summary.items():
        print(f"{k}: {v:.2f}" if isinstance(v, float) else f"{k}: {v}")

    # Save output
    if output_file.endswith('.csv'):
        df.to_csv(output_file, index=False)
    else:
        df.to_excel(output_file, index=False)

    print(f"\nCleaned file saved: {output_file}")
    print("Ready for freelance use – clean, commented, and reliable!")

except Exception as e:
    print(f"Error occurred: {e}")