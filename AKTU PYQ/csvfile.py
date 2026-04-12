import pandas as pd

# Read CSV file
df = pd.read_csv('E:/DSA/A. Python Programs/AKTU PYQ/data.csv')

# Column name and threshold
column_name = 'Marks'      # change as per your CSV
threshold = 50

# Filter rows
filtered_data = df[df[column_name] > threshold]

# Display result
print(filtered_data)