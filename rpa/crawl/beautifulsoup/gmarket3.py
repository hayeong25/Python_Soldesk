# Gmarket best - 컴퓨터/전자 항목 추출

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook()
ws = wb.active()

# A 컬럼 width 조절
ws.column_dimensions["A"].width = 70

# 시트명 새로 지정
ws.title = "Gmarket Best"

# 제목행 지정
ws.append(["순위", "제품명", "가격"])

URL = "http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G06"
res = requests.get(URL)
soup = BeautifulSoup(res.text, "lxml")

list = soup.select(".first")
for idx, item in enumerate(list, 1):
    # 타이틀
    name = item.select_one(
        "#gBestWrap > div > div:nth-child(5) > div > ul > li > a"
    ).get_text()
    # 신문사
    price = item.select_one(
        "#gBestWrap > div > div:nth-child(5) > div > ul > li > div.item_price > div.s-price > strong > span > span"
    ).get_text()
    ws.append(f"{idx}. {name} - {price}")

# 엑셀 저장

ws.save("./rpa/crawl/download/" + filename)
