# clien 팁과 강좌 게시판 크롤링
import requests
import datetime
from openpyxl import Workbook
from bs4 import BeautifulSoup

wb = Workbook()

# 기본 시트 활성화
ws = wb.active()

# A 컬럼 width 조절
ws.column_dimensions["A"].width = 70

# 시트명 새로 지정
ws.title = "팁과 강좌"

# 제목행 지정
ws.append(["글제목", "작성일"])

res = requests.get("https://www.clien.net/service/board/lecture")
soup = BeautifulSoup(res.text, "lxml")

# 게시판 제목 가져오기
title_list = soup.select("a.list_subject > span.subject_fixed")
for title in title_list:
    print(title.get_text().strip())

for page_num in range(5):
    if page_num == 0:  # 1 page
        res = requests.get("https://www.clien.net/service/board/lecture")
    else:
        res = requests.get(
            "https://www.clien.net/service/board/lecture?od=T31&category=0&po="
            + str(page_num)
        )

# 파일명
today = datetime.now().strftime("%y%m%d")
filename = f"clien_{today}.xlsx"

# 엑셀 저장
wb.save("./rpa/crawl/download/" + filename)
