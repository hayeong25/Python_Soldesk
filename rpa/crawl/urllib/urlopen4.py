from base64 import decode
import urllib.request as req

# 영화진흥위원회 어제 날짜 박스오피스 파일 저장

# 다운 받을 경로
path = "./rpa/crawl/download/"

try:
    url = "https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=4d8b303b3f7ea8a972177a97cd626b1c&targetDt=20220608"
    contents = req.urlopen(url).read().decode
except Exception as e:
    print(e)
else:
    with open(path + "movie.txt", "w", encoding="UTF-8") as f:
        f.write(contents)
    print("성공")
