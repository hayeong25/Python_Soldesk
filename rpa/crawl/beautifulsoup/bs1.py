# requests + beautifulsoup4
# 객체 생성(페이지소스, 파서)

from urllib import request
import requests

from bs4 import BeautifulSoup

res = requests.get("https://news.v.daum.net/v/20220613094332521")
print(res.text)

# parser : html.parser(설치 필요 X)
soup = BeautifulSoup(res.text, "html.parser")
soup = BeautifulSoup(res.text, "lxml")  # lxml이 더 빠름
print(soup)
print(soup.prettify())  # 자동 정렬 후 출력

# <head> 태그 안의 내용 가져오기
print(soup.head)

# <body> 태그 안의 내용 가져오기
print(soup.body)

# <title> 태그 안의 내용 가져오기
print(soup.title)
print(soup.title.name)  # 태그명 가져오기
print(soup.title.get_text())  # 태그 안 텍스트 가져오기
print(soup.title.string)  # 태그 안 텍스트 가져오기

# 문서 가져오기
res = requests.get("https://news.v.daum.net/v/20220613091424213")
soup = BeautifulSoup(res.text, "lxml")

# 기사 제목 가져오기
print("기사 제목 : {}".format(soup.find("h3")))

# 기사 작성 날짜와 시간 가져오기
print("작성 날짜 및 시간 : {}".format(soup.find(class_="num-date")))

# 기사 작성자 가져오기
print("작성자 : {}".format(soup.find(class_="txt-info")))

# 기사 첫 번째 문단 가져오기
print("기사 첫 번째 문단 : {}".format(soup.find("p")))
