from sys import orig_argv
from unicodedata import category
import requests
from bs4 import BeautifulSoup

url = "http://rpp.gmarket.co.kr/?exhib=56449&jaehuid=200010616"

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

# 1차 카테고리 추출
one_depth = soup.find_all("a", class_="list_1depth-item", limit=9)

for item in one_depth:
    print(item.get_text())

# 2차 카테고리 추출
two_depth = soup.find("li", class_="list-item__2depth", limit=69)

print(len(two_depth))

# get_text() : 태그(자식태그 포함)가 가지고 있는 모든 문자열 가져오기
# string : 태그가 가지고 있는 문자열만 가지고 오기
for item in two_depth:
    print(item)
    print(item.string)

for depth in two_depth:
    href = depth.find("a")
    print(href)
