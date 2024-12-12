import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = "/home/solo/Desktop/converts/mattanalysis.xlsx"  
data = pd.read_excel(file_path, sheet_name=0)

# Inspect the data
print("Data Overview:")
print(data.info())
print("\nSample Data:")
print(data.head())

# Handle Missing Data
print("\nChecking for missing values:")
print(data.isnull().sum())

# Convert 'Date' to datetime
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

data['Paid In'] = pd.to_numeric(data['Paid In'], errors='coerce')
data['Withdrawn'] = pd.to_numeric(data['Withdrawn'], errors='coerce')
data['Balance'] = pd.to_numeric(data['Balance'], errors='coerce')

# Drop rows where 'Date' is missing (critical for analysis)
data = data.dropna(subset=['Date'])

# Drop columns with all NaN values
data = data.dropna(how='all', axis=1)  

data = data.drop_duplicates(subset=['Receipt No.'])

# Clean and convert 'Paid In', 'Withdrawn', and 'Balance' columns
for col in ['Paid In', 'Withdrawn', 'Balance']:
    if col in data.columns:
        data[col] = (
            data[col]
            .astype(str)                      # Ensure all data is string for cleaning
            .str.replace(",", "")             # Remove commas
            .str.replace("-", "0")            # Replace dashes with zeros
            .str.strip()                      # Remove leading/trailing spaces
        )
        data[col] = pd.to_numeric(data[col], errors='coerce')  # Convert to numeric
        data[col] = data[col].fillna(0)  # Replace NaNs with 0

# Add a Month column for monthly analysis
data['Month'] = data['Date'].dt.to_period('M')

# Total 'Paid In' and 'Withdrawn' by Month
monthly_summary = data.groupby('Month').agg({
    'Paid In': 'sum',
    'Withdrawn': 'sum'
})
print("\nMonthly Summary:")
print(monthly_summary)

# Save Monthly Summary to CSV
monthly_summary.to_csv("monthly_summary.csv")

# Plot Monthly 'Paid In' and 'Withdrawn'
monthly_summary.plot(kind='bar', figsize=(10, 6), color=['green', 'red'])
plt.title("Monthly Paid In vs. Withdrawn")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_paid_in_vs_withdrawn.png")  # Save figure as PNG

# Daily Balance Trend
if 'Date' in data.columns and 'Balance' in data.columns:
    daily_balance = data.groupby('Date')['Balance'].last()  # Use last balance of the day
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=daily_balance, marker="o", color="blue")
    plt.title("Daily Balance Trend")
    plt.xlabel("Date")
    plt.ylabel("Balance")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("daily_balance_trend.png")  # Save figure as PNG

# Save cleaned data to Excel
cleaned_file_path = "/home/solo/Desktop/converts/cleaned_mattanalysis.xlsx"
data.to_excel(cleaned_file_path, index=False)

print(f"\nOutput files saved:\n- Monthly summary CSV: monthly_summary.csv\n- Monthly bar chart: monthly_paid_in_vs_withdrawn.png\n- Daily balance trend: daily_balance_trend.png\n- Cleaned data Excel: {cleaned_file_path}")
