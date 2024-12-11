import pandas as pd

# Load the Excel file
file_path = "/home/solo/Desktop/converts/summarystatement.xlsx" 
output_path = "/home/solo/Desktop/converts/merged_file.xlsx"

# Read all sheets
excel_data = pd.ExcelFile(file_path, engine='openpyxl')
merged_data = pd.DataFrame()

# Append each sheet to the merged DataFrame
for sheet_name in excel_data.sheet_names:
    sheet_data = excel_data.parse(sheet_name)
    sheet_data['SheetName'] = sheet_name  # Optional: Add a column for sheet identification
    merged_data = pd.concat([merged_data, sheet_data], ignore_index=True)

# Save to a new Excel file
merged_data.to_excel(output_path, index=False)

print(f"All sheets merged into {output_path}")
