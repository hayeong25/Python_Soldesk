import random
from openpyxl import Workbook

wb = Workbook()

# 기본 시트 활성화
ws = wb.active

# 시트 이름 변경
ws.title = "test"

# 셀에 데이터 입력
for x in range(1, 11):
    for y in range(1, 11):
        ws.cell(row=x, column=y, value=random.randint(0, 100))

wb.save("./rpa/excel/sample.xlsx")
