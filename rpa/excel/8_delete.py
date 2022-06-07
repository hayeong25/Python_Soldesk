from openpyxl import load_workbook

wb = load_workbook("./rpa/excel/range.xslx")
ws = wb.active

# 특정 행 삭제
ws.delete_rows(8, 3)  # 8번 행부터 3개 행 삭제

# 특정 열 삭제
ws.delete_cols(1, 2)  # 2번 열 삭제

wb.save("./rpa/excel/range_delete.xslx")
