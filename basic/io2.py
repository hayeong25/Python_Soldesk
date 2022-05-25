# 파일 읽기

with open("data/review.txt", "r", encoding="UTF-8") as f:
    print(f.read())

# readline() : 줄 단위로 읽어오기
with open("data/review.txt", "r", encoding="UTF-8") as f:
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()

# 파일 내용을 list로 가져오기
with open("data/review.txt", "r", encoding="UTF-8") as f:
    print(f.readlines())

# score.txt 읽어와서 평균 출력하기
score = []
with open("data/score.txt", "r", encoding="UTF-8") as f:
    for num in f:
        score.append(int(num))
    print(score)
print("평균 : %.2f" % (sum(score) / len(score)))

# 총합과 평균을 result.txt 파일로 작성
with open("data/result.txt", "w", encoding="UTF-8") as f:
    f.write("총합 : %d\n" % sum(score))
    f.write("평균 : %.2f" % (sum(score) / len(score)))

# info.txt 읽어온 후 BMI 지수를 계산해 화면 출력
with open("data/info.txt", "r", encoding="UTF-8") as f:
    while f.readline():
        name, weight, height = f.readline().split(",")
        BMI = int(weight) / (int(height) / 100) ** 2
        if BMI >= 25:
            result = "과체중"
        elif BMI >= 18.5:
            result = "정상체중"
        else:
            result = "저체중"
        print(name, weight, height, BMI, result)

# 원본 파일을 읽은 후 암호화, 암호화 된 파일을 읽은 후 복호화 하는 프로그램 작성
content = ""
while True:
    no = int(input("1. 암호화 | 2. 복호화 | 3. 종료 : "))

    if no == 1:
        # origin.txt 읽어와서 content 변수에 담기
        with open("data/origin.txt", "r", encoding="UTF-8") as f:
            content = f.read()
        # encryption.txt 작성 및 content 암호화
        with open("data/encryption.txt", "w", encoding="UTF-8") as f:
            for c in content:
                f.write(chr(ord(c) + 100))
    elif no == 2:
        # encryption.txt 읽어와 원래 내용으로 출력
        with open("data/encryption.txt", "r", encoding="UTF-8") as f:
            content = f.read()
            for i in range(0, len(content)):
                print(chr(ord(content[i]) - 100), end="")
    else:
        print("프로그램을 종료합니다")
        break
    print()

# r, w, rb, wb => b가 붙으면 이진 파일
data = None
with open("c:\\windows\\notepad.exe", "rb") as f:
    data = f.read()
with open("c:\\temp\\notepad.exe", "wb") as f:
    f.write(data)
