# https://news.nate.com/rank/interest?sc=ent 랭킹 뉴스 추출
# 제목, 신문사명, 1위 ~ 50위

import requests
from bs4 import BeautifulSoup

URL = "https://news.nate.com/rank/interest?sc=ent"
res = requests.get(URL)
soup = BeautifulSoup(res.text, "lxml")

# 상위 랭킹
top_list = soup.select("div.mduSubjectList > div")
for idx, news in enumerate(top_list, 1):
    # 타이틀
    title = news.select_one("a strong").get_text()
    # 신문사
    media = news.select_one("span.medium").get_text()
    print(f"{idx}. {title} - {media}")

# 6위 ~ 50위
list = soup.select("#postRankSubject li")
for idx, news in enumerate(list, 1):
    # 타이틀
    title = news.select_one("a").get_text()
    # 신문사
    media = news.select_one("span.medium").get_text()
    print(f"{idx}. {title} - {media}")
