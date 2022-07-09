import urllib.request as req

target_url = [
    "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA1MTBfMjU1%2FMDAxNjUyMTYzMDI5NTIy.ppamGH0wkCpjODW73XnUoDpOuqYaSWIsma_CfXFzxLAg.kocnNWxM6WNp-nC7GHuI14kihiMr087ofOMpFegVtLog.JPEG.dlscksspwlq%2F%25BF%25C0%25BB%25EA%25B0%25ED%25BE%25E7%25C0%25CC%25BA%25D0%25BE%25E7_%25287%2529.jpg&type=sc960_832",
    "https://www.naver.com",
]

# 다운로드 받을 경로
path_list = ["./rpa/crawl/download/cat.png", "./rpa/crawl/download/naver.html"]

for i, url in enumerate(target_url):
    try:
        res = req.urlopen(url)
        contents = res.read()
        print("----------------------------")
        print("Header info - {} : {}".format(i, res.info()))
        print("HTTP status : {}".format(res.getcode()))
        print("----------------------------")
        with open(path_list[i], "wb") as c:
            c.write(contents)
    except Exception as e:
        print(e)
    else:
        print("성공")
