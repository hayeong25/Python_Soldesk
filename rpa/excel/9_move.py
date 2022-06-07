# 셀 이동

from openpyxl import load_workbook

wb = load_workbook("./rpa/excel/range.xslx")
ws = wb.active

# rows는 그대로 놔두고, cols만 오른쪽으로 한 칸 이동 (음수는 왼쪽/위 로 이동)
ws.move_range("B1:C11", rows=0, cols=1)  # B1 ~ C11의 데이터를 다른 곳으로 이동시키기

wb.save("./rpa/excel/range_move.xslx")
