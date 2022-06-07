from openpyxl import load_workbook

wb = load_workbook("./rpa/excel/range.xslx")
ws = wb.active

# 행 삽입
ws.insert_rows(8, 5)  # 8번 행부터 5개 행 삽입

# 열 삽입
ws.insert_cols(2, 3)  # 2번 열부터 3개 열 삽입

wb.save("./rpa/excel/range.xslx")
