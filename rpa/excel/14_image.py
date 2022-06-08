# 엑셀에 이미지 삽입

from openpyxl import Workbook
from openpyxl.drawing.image import Image  # Image 객체 불러오기

wb = Workbook()
ws = wb.active

imf = Image("./rpa/excel/ssol_logo.png")

ws.add_image(img, "C3")

wb.save("./rpa/excel/image.xlsx")
