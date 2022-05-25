# dictionary 자료 구조 - Java의 Map과 같은 개념
# key, value를 한 쌍으로 갖는 자료형 {key:value}
# dictionary => JSON / JSON => dictionary 많이 사용

dict1 = {"name": "park", "age": 12}
dict2 = {0: "Hello Python", 1: "Hello coding"}
dict3 = {"arr": [0, 1, 2, 3, 4]}
print(dict1)
print(dict2)
print(dict3)

# dictionary에서 원하는 값 가져오기 : [key]
print(dict1["age"])
# print(dict1["addr"])  # KeyError

# dictionary에 쌍 추가
dict1["birth"] = "1115"
print(dict1)

dict2[2] = ["Hello Java", "Hello JSP"]
print(dict2)

dict3["rank"] = (16, 17, 18)
print(dict3)

# dictionary 쌍 삭제
del dict1["birth"]
print(dict1)

# === 실습 ===
# numbers 내부에 들어있는 숫자가 각각 몇 번 등장하는지 dictionary로 작성하여 출력
numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
cnt = {}
for i in numbers:
    cnt[i] = numbers.count(i)
print(cnt)

# keys() : key만 모아서 보여줌
print(dict1.keys())
print(dict3.keys())

# values() : value만 모아서 보여줌
print(dict1.values())
print(dict2.values())
print(dict3.values())

# items() : key, value 쌍 가져오기
print(dict1.items())
print(dict2.items())
print(dict3.items())

# get() : key로 value 가져오기
print(dict1.get("age"))
print(dict1.get("age"))  # None => Error는 안 남

# in : 해당 key가 dictionary 안에 있는지 확인
print("name" in dict1)
print(4 in dict2)
print("rank" in dict3)

my_info = {"name": "kim", "age": 30, "city": "seoul"}
for k in my_info.keys():
    print(k)
for v in my_info.values():
    print(v)
for k, v in my_info.items():
    print(k, v)

# === 실습 ===
dict1 = {"A": 90, "B": 80, "C": 70}
# dict1에서 B 값만 출력
print(dict1["B"])
# B 삭제 후 dict1
del dict1["B"]
print(dict1)

dict2 = {"성인": 100000, "청소년": 70000, "어린이": 30000}
# dict2에 소아:0 추가
dict2["소아"] = 0
print(dict2)
# key만 출력
print(dict2.keys())
# value만 출력
print(dict2.values())
