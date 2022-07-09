# 네이버 오픈 API 이용하기

import requests

client_id = "ObR7t_ig_MksARWbtN86"
client_secret = "RH_A6LmYyr"

headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}

start = 1
for idx in range(10):
    start_num = start + (idx * 100)

    URL = (
        "https://openapi.naver.com/v1/search/shop.json?query=키보드&display=100&start="
        + str(start_num)
    )

    print(URL)

    res = requests.get(URL, headers=headers)

    # JSON 데이터 확인
    data = res.json()
    for item in data["items"]:
        print(item["title"])
