from bs4 import BeautifulSoup

# 문서 가져오기
with open("./rpa/crawl/beautifulsoup/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "lxml")
print(soup.prettify())

# 첫 번째 p 태그
p1 = soup.find("p")
print(p1)

# 두 번째 p 태그
p2 = soup.find("p", class_="story")  # 구조적으로 찾지 않고 필요한 것을 직접 찾으러 감
print(f"p 두 번째 >> {p2}")
print(f"p 두 번째 내용 >> {p2.get_text()}")
print(f"p 두 번째 속성들 >> {p2.attrs}")
print(f"p 두 번째 특정 속성 값 >> {p2['class']}")

p3 = p2.find_next_sibling("p")
print(f"p 세 번째 >> {p3}")
print(f"p 세 번째 내용 >> {p3.get_text()}")
print(f"p 세 번째 속성들 >> {p3.attrs}")
print(f"p 세 번째 특정 속성 값 >> {p3['class']}")

# 첫 번째 a
a1 = soup.find("a")

# 두 번째 a
a2 = soup.find("a", id="link2")
print(f"a 두 번째 >> {a2}")
print(f"a 두 번째 내용 >> {a2.get_text()}")
print(f"a 두 번째 속성들 >> {a2.attrs}")
print(f"a 두 번째 특정 속성 값 >> {a2['class']}")

# 세 번째 a
a3 = soup.find("a", id="link3")
a3 = soup.find("a", class_="sister", id="link3")
# 속성을 딕셔너리 형태로도 찾을 수 있음
a3 = soup.find(
    "a",
    attrs={"class": "sister", "id": "link3", "data-io": "tillie"},
)
print(f"a 세 번째 >> {a3}")
print(f"a 세 번째 내용 >> {a3.get_text()}")
print(f"a 세 번째 속성들 >> {a3.attrs}")
print(f"a 세 번째 특정 속성 값 >> {a3['href']}")

# find_all() : 모두 가져오기 때문에 리스트 구조로 return
a = soup.find_all("a")
print(a)

# limit : 개수 지정해서 가지고 오기
a = soup.find_all("a", limit=2)
print(a)

a = soup.find_all("a", class_="sister")
print(a)

# text node 값 이용해서 가져오기
a = soup.find_all(string=["Elsie"])
print(a)
