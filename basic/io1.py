# 파일 읽고 쓰기

# open("파일명", 모드, encoding 여부, ...) : 파일을 읽거나 쓸 때 사용하는 함수
# with + open() : f.close() 자동으로 해줌
# w : write(쓰기) 모드. 기존 내용 무시하고 새로 작성
# a : 기존 내용 뒤에 덧붙이기
f = open("data/test1.txt", "w", encoding="UTF-8")
f.write("안녕하세요\n반값습니다")
f.close()
print(dir(f))  # FileNotFoundError (Java에서는 FileNotFoundException)

# with open("data/test1.txt", "w", encoding="UTF-8") as f:
#     f.write("안녕하세요")

# 1 ~ 10까지 파일로 작성
f = open("data/test1.txt", "a", encoding="UTF-8")
for i in range(1, 11):
    f.write("%d\t" % i)
f.close()

# with open("data/test1.txt", "a", encoding="UTF-8") as f:
#     for i in range(1, 11):
#         f.write("%d\t" % i)

# list를 파일로 작성
list = ["김모씨", "박모씨", "최모씨", "이모씨", "양모씨"]
f = open("data/test1.txt", "w", encoding="UTF-8")
# f.write(list)  # TypeError : write() argument must be str, not list
# f.writelines(list)
for i in list:
    f.write(i + " ")
f.close()

# dictionary 형태를 파일로 작성
dict1 = {"name": "kim", "age": 26, "address": "seoul"}
f = open("data/test1.txt", "w", encoding="UTF-8")
# f.writelines(dict1) # key값만 기록됨
for k, v in dict1.items():
    f.writelines("{} : {}\n".format(k, v))
f.close()

# 1000명의 키와 몸무게를 랜덤으로 생성한 후 파일로 작성
import random

list1 = list("가나다라마바사아자차카타파하")
f = open("data/info.txt", "w", encoding="UTF-8")
for i in range(1000):
    name = random.choice(list1) + random.choice(list1)
    weight = random.randrange(40, 100)  # 40 ~ 100 사이의 임의의 숫자
    height = random.randrange(140, 200)
    f.writelines("{}, {}, {}\n".format(name, weight, height))
f.close()
