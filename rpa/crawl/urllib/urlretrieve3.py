import urllib.request as req

# 이미지, HTML 파일 다운로드
img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA1MTdfMzcg%2FMDAxNjUyNzQ1NDI2NTE3.SwCdooJ2oc9xqVaGSDYDbJIqb0uT05SY57vEqvyTs2cg.f-8PpYHXdWziz9JOJ71ncKSJ6690MNG_M-nafvIrYZ8g.JPEG.dlalswjddl2%2F20220428%25A3%25DF181642.jpg&type=sc960_832"
file_url = "https://www.naver.com"

# 다운로드 받을 경로
path = "./rpa/crawl/download/"

try:
    file1, header1 = req.urlretrieve(img_url, path + "pasta.png")
    file2, header2 = req.urlretrieve(file_url, path + "naver.html")
except Exception as e:
    print(e)
else:
    print(header1)
    print(header2)
