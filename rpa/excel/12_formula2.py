# 함수 삽입
from openpyxl import load_workbook
from datetime import datetime

wb = load_workbook("./rpa/excel/formula.xlsx")
ws = wb.active

for row in ws.values:
    for cell in row:
        print(cell)

wb.save("./rpa/excel/formula.xlsx")
