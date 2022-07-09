# clien 팁과 강좌 게시판 크롤링
import requests
from bs4 import BeautifulSoup

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
