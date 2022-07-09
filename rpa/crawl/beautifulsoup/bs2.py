from email import header
from urllib import request
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = "https://n.news.naver.com/mnews/article/018/0005240441?sid=103"
headers = {"user-agent": UserAgent().chrome}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")

# 특정 요소 찾기 - 1. 태그 이용 (가장 처음에 만나는 태그만 가져오기)
print(soup.h2)

# 특정 요소 찾기 - 1. find(), find_all()
h2_element = soup.find("h2", class_="media_end_head_headline")
print(h2_element)
