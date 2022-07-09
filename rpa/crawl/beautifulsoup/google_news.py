# 구글 뉴스 클리핑

import requests
from bs4 import BeautifulSoup


def main():
    url = "https://news.google.com/search?q=파이썬&hl=ko&gl=KR&ceid=KR%3Ako"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")

    data_extract(soup)


def data_extract(soup):
    # 원하는 요소 추출
    news_list = []
    news_item = {}

    # 뉴스 원문 url, 제목, 출처, 등록일
    # 각 개별 기사는 dict 구조로 생성
    articles = soup.select("div.xrnccd")
    for article in articles:
        # 제목과 링크 가지고 있는 태그 요소 찾기
        link_title = article.select_one("h3 > a")
        base_url = "https://news.google.com"
        href = base_url + link_title["href"][1:]
        title = link_title.get_text()
        print(title + href)

        # 출처 및 뉴스 보도 시간 가지고 있는 태그 요소 찾기
        writer_time = article.select_one("div.SVJrMe")

        # 출처만 추출
        writer = writer_time.select_one("a").get_text()

        # 시간만 추출
        date_time = writer_time.select_ont("time")

        if date_time:
            report_date_time = date_time["datetime"].split("T")
            report_date = report_date_time[0]
            report_time = report_date_time[1]
        else:
            report_date = ""
            report_time = ""

        print(title, href, report_date, report_time)

    # 리스트 return


if __name__ == "__name__":
    main()
