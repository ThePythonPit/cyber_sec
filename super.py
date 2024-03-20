import pandas as pd

file_path = 'C:\\Users\\J\\Desktop\\cybersec-prototype\\super.xls'  # Adjust path as necessary


tables = pd.read_html(file_path)
data = tables[0]  # Assuming your data is in the first table
print(data.head())
# Attempt to determine the correct engine based on file extension
if file_path.endswith('.xlsx'):
    engine = 'openpyxl'
else:
    engine = 'xlrd'  # For older .xls files

try:
    data = pd.read_excel(file_path, engine=engine)
    print(data.head())  # Or proceed with your data analysis
except ValueError as e:
    print(f"Failed to read Excel file with specified engine '{engine}': {e}")

