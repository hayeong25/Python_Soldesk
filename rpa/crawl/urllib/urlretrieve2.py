import urllib.request as req

# 이미지, HTML 파일 다운로드
img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA1MTBfMjU1%2FMDAxNjUyMTYzMDI5NTIy.ppamGH0wkCpjODW73XnUoDpOuqYaSWIsma_CfXFzxLAg.kocnNWxM6WNp-nC7GHuI14kihiMr087ofOMpFegVtLog.JPEG.dlscksspwlq%2F%25BF%25C0%25BB%25EA%25B0%25ED%25BE%25E7%25C0%25CC%25BA%25D0%25BE%25E7_%25287%2529.jpg&type=sc960_832"
file_url = "https://www.naver.com"

# 다운로드 받을 경로
path = "./rpa/crawl/download/"

try:
    file1, header1 = req.urlretrieve(img_url, path + "cat.png")
    file2, header2 = req.urlretrieve(file_url, path + "naver.html")
except Exception as e:
    print(e)
else:
    print(header1)
    print(header2)
