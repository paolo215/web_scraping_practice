# Libary for reading xlsx
import xlrd

# Open workbook
workbook = xlrd.open_workbook("master.xlsx")

# Get default worksheet
worksheet = workbook.sheet_by_index(0)


# Number of rows in this spreadsheet
rows = worksheet.nrows


# Go over the rows
for row in range(rows):
    first, second = worksheet.row_values(row) # Returns a tuple
    print(first, second)


