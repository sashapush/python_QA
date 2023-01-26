import openpyxl

book = openpyxl.load_workbook("C:\\Users\\Alex\\Documents\\DemoFile.xlsx")
sheet = book.active
cell = sheet.cell(row=1, column=2)
print(cell.value)
sheet.cell(row=2, column=2).value = "Sapushka"  # assigning value to the doc
