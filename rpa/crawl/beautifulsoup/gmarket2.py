# Gmarket best - 컴퓨터/전자 항목 추출

import requests
from bs4 import BeautifulSoup

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
    print(f"{idx}. {name} - {price}")
