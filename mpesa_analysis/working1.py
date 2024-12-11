import subprocess
from tabula import read_pdf
import pandas as pd

# Decrypt the PDF
input_pdf = "/home/solo/Desktop/converts/2024.pdf"
output_pdf = "/home/solo/Desktop/converts/decrypted.pdf"
password = "679534"

try:
    subprocess.run(
        ["qpdf", "--decrypt", f"--password={password}", input_pdf, output_pdf],
        check=True
    )
    print("PDF decrypted successfully.")
except subprocess.CalledProcessError as e:
    print("Failed to decrypt PDF:", e)
    exit(1)

# Extract tables from the decrypted PDF
tables = read_pdf(output_pdf, pages="all", multiple_tables=True)

# Save all tables into a single Excel file
output_excel = "all_tables.xlsx"
with pd.ExcelWriter(output_excel) as writer:
    for i, table in enumerate(tables):
        table.to_excel(writer, sheet_name=f"Table_{i+1}", index=False)

print(f"All tables have been saved to {output_excel}")
