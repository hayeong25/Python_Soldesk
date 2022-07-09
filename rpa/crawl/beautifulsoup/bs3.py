from bs4 import BeautifulSoup

# 문서 가져오기
with open("./rpa/crawl/beautifulsoup/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "lxml")
print(soup.prettify())

# 1. 태그명으로 찾기
title = soup.title
print("title >> {}".format(title))
print("title 내용 >> {}".format(title.get_text()))
print("title 부모 태그 >> {}".format(title.parent))

# h1 태그 찾기
h1 = soup.h1
print("h1 >> {}".format(h1))
print("h1 내용 >> {}".format(h1.get_text()))

# h2 태그 찾기
h2 = soup.h2
print("h2 >> {}".format(h2))
print("h2 내용 >> {}".format(h2.get_text()))

p1 = soup.p
print(f"p >> " {p1})
print(f"p 내용 >> " {p1.get_text()})
print(f"p 태그 속성들 >> " {p1.attrs})
print(f"p 태그 특정 속성 값 >> " {p1['class']})

# a 출력
print(f"b >> " {soup.b})
print(f"b 내용 >> " {soup.b.get_text()})

# b 출력
print(f"b >> " {soup.b})
print(f"b 내용 >> " {soup.b.get_text()})