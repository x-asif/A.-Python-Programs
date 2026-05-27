# import pandas as pd

# # Read CSV file
# df = pd.read_csv('E:/DSA/A. Python Programs/AKTU PYQ/data.csv')
# data = {
#     "Name":["Asif", "Arif", "Raja"], "Roll":[40,41,42]
# }

# # new changes

# print(data.values())
# print(pd.DataFrame(data))

# # Column name and threshold
# # column_name = 'Marks'      # change as per your CSV
# # threshold = 50

# # # Filter rows
# # filtered_data = df[df[column_name] > threshold]

# # Display result
# print(df)















# import pandas as pd
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# from reportlab.lib.styles import getSampleStyleSheet

# # Read CSV file
# df = pd.read_csv('E:/DSA/A. Python Programs/AKTU PYQ/data.csv')

# # Your dictionary data
# data = {
#     "Name": ["Asif", "Arif", "Raja"],
#     "Roll": [40, 41, 42]
# }

# df2 = pd.DataFrame(data)

# # Create PDF
# pdf = SimpleDocTemplate("output.pdf")
# styles = getSampleStyleSheet()

# content = []

# # Title
# content.append(Paragraph("CSV Data:", styles['Heading2']))
# content.append(Spacer(1, 10))

# # CSV data
# for i in df.values:
#     content.append(Paragraph(str(i), styles['Normal']))
#     content.append(Spacer(1, 5))

# # Space
# content.append(Spacer(1, 20))

# # Dictionary Data
# content.append(Paragraph("Dictionary Data:", styles['Heading2']))
# content.append(Spacer(1, 10))

# for i in df2.values:
#     content.append(Paragraph(str(i), styles['Normal']))
#     content.append(Spacer(1, 5))

# # Build PDF
# pdf.build(content)

# print("PDF created successfully!")




import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Read CSV file
df = pd.read_csv('E:/DSA/A. Python Programs/AKTU PYQ/data.csv')

# Dictionary data
data = {
    "Name": ["Asif", "Arif", "Raja"],
    "Roll": [40, 41, 42]
}
df2 = pd.DataFrame(data)

# Create PDF
pdf = SimpleDocTemplate("output.pdf")
styles = getSampleStyleSheet()

content = []

# ------------------ TITLE ------------------
content.append(Paragraph("<b><font color='blue'>CSV FILE AND PANDAS REPORT</font></b>", styles['Title']))
content.append(Spacer(1, 20))

# ------------------ CSV THEORY ------------------
csv_text = """
<b>What is a CSV File?</b><br/>
CSV (Comma Separated Values) is a file format used to store tabular data such as tables or spreadsheets.
Each line represents a row and values are separated by commas. It is widely used for data exchange
because it is simple and supported by many applications.
"""
content.append(Paragraph(csv_text, styles['Normal']))
content.append(Spacer(1, 15))

# ------------------ HANDLING CSV ------------------
handling_text = """
<b>Handling CSV Files in Python:</b><br/>
CSV files can be handled easily using the Pandas library. Pandas provides functions to read,
write and manipulate data efficiently.<br/>
Example: <br/>
- read_csv() → Used to read CSV file<br/>
- to_csv() → Used to write data into CSV file
"""
content.append(Paragraph(handling_text, styles['Normal']))
content.append(Spacer(1, 15))

# ------------------ PANDAS FEATURES ------------------
pandas_text = """
<b>Pandas Features and Methods:</b><br/>
- DataFrame → Main data structure in Pandas<br/>
- head() → Shows first 5 rows<br/>
- tail() → Shows last 5 rows<br/>
- info() → Displays summary of data<br/>
- describe() → Statistical summary<br/>
- shape → Returns number of rows and columns<br/>
- columns → Returns column names<br/>
- filtering → Select data using conditions
"""
content.append(Paragraph(pandas_text, styles['Normal']))
content.append(Spacer(1, 20))

# ------------------ CSV DATA TABLE ------------------
content.append(Paragraph("<b><font color='green'>CSV Data</font></b>", styles['Heading2']))
content.append(Spacer(1, 10))

table_data = [list(df.columns)] + df.values.tolist()

table = Table(table_data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige)
]))

content.append(table)
content.append(Spacer(1, 20))

# ------------------ DICTIONARY DATA ------------------
content.append(Paragraph("<b><font color='green'>Dictionary Data</font></b>", styles['Heading2']))
content.append(Spacer(1, 10))

table_data2 = [list(df2.columns)] + df2.values.tolist()

table2 = Table(table_data2)
table2.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey)
]))

content.append(table2)

# ------------------ BUILD PDF ------------------
pdf.build(content)

print("Colored PDF created successfully!")