# Libary for writing to xlsx
from xlsxwriter import Workbook

# Create workbook
workbook = Workbook("master.xlsx")

# Add spreadsheet
worksheet = workbook.add_worksheet()

for row in range(20):
    worksheet.write(row, 0, "Number")
    worksheet.write(row, 1, row)

workbook.close()


