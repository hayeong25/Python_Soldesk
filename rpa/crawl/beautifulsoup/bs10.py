import requests
from bs4 import BeautifulSoup

res = requests.get("https://")
soup = BeautifulSoup(html, "lxml")

# h1 태그 가져오기
h1 = soup.select_one("h1")

# 상단 내용 가져오기
top = soup.select_one("")

# 모든 img 태그 가져오기
img = soup.select("img")

# 타이틀 행 가져오기
title = soup.select_one("title")

# 테이블 내용 가져오기
table = soup.select_one("table")

# 가격만 가져오기
price = soup.select_one("price")
