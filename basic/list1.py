# list - 배열과 비슷하지만 다양한 형태의 자료들을 담을 수 있음

# 생성
list1 = []
list2 = list(["a", "b", "c"])
list3 = ["a", "b", "c", 1, 2]
list4 = [1, 2, 3, 4, 5, 6.5]
list5 = [1, 2, ["Life", "is", "short"]]
list6 = list()

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)

# 인덱싱
print("list2[0] :", list2[0])
print("list3[-1] :", list3[-1])
print("list4[3] :", list4[3])
print("list4[3] + list5[1] :", (list4[3] + list5[1]))

# 슬라이싱
print("list2[0:3]", list2[0:3])
print("list3[1:3] :", list3[1:3])
print("list5[2:] :", list5[2:])

# is 출력
list6 = [1, 2, ["a", "b", ["Life", "is"]]]
print(list6[2][2][1])

# 연산자
# + : 연결, 산술연산(인덱싱)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = ["a", "b", "c"]

print("list1 + list2 = ", (list1 + list2))
print("list1 + list3 = ", (list1 + list3))
print("list1[0] + list2[1] = ", (list1[0] + list2[1]))
print("list1[0] + list3[1] = ", (list1[0] + list3[1]))

# *
print("list1 * 3", list1 * 3)

# 리스트 요소 값 변경
print("list1 = ", list1)
list1[1] = 7
print("list1 = ", list1)
list1[2] = "Life"
print("list1 = ", list1)

print("list2 = ", list2)
list2[1:2] = [10, 11]
print("list2 = ", list2)
list2[1] = [15, 16, 17]  # list 속의 list로 삽입됨
print("list2 = ", list2)

# 리스트 요소 삭제
print("list1 = ", list1)
del list1[0]
print("list1 = ", list1)
del list1[2:3]
print("list1 = ", list1)

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
for num in list1:
    print(num, end=" ")

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# 리스트 안의 숫자 중 100 이상인 숫자 출력
for i in numbers:
    if i >= 100:
        print(i, end=" ")

# 리스트 안의 숫자가 홀수/짝수인지 판별하기
for i in numbers:
    if i % 2 == 0:
        print("홀수", end=" ")
    else:
        print("짝수", end=" ")

# 리스트 안의 숫자들 자릿수 출력
for i in numbers:
    print("{}은 {}자리".format(i, len(str(i))))

# append() : 리스트에 요소 추가
list1 = [1, 2, 3]
list1.append(4)
list1.append([5, 6, 7])  # list로 삽입
print(list1)

# 1 ~ 100까지의 숫자 중에서 짝수 리스트 생성
even = []
for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
print(even)

# sort() : 정렬
list1 = [1, 4, 3, 2]
print("정렬 전 : ", list1)
list1.sort()
print("정렬 후 : ", list1)

list2 = ["k", "z", "a", "b", "a"]
print("정렬 전 : ", list2)
list2.sort(reverse=True)  # reverse=True : 내림차순 정렬
print("정렬 후 : ", list2)

list3 = ["ㄷ", "ㄱ", "ㅁ", "ㅅ", "ㄴ"]
print("정렬 전 : ", list3)
list3.sort()
print("정렬 후 : ", list3)

# reverse() : list 뒤집기
list1 = ["a", "c", "b", "z"]
print("reverse 전 :", list1)
list1.reverse()
print("reverse 후 :", list1)

# sort() + reverse() : 내림차순 정렬
list1[3, 12, 1, 5, 9, 2, 7]
print("정렬 전 : ", list1)
list1.sort()
list1.reverse()
print("정렬 후 : ", list1)

# index() : 위치 반환
print("list1", list1)
print("list1에 9가 있는지 확인 : ", list1.index(9))  # 1 (1번 요소)
print("list1에 45가 있는지 확인 : ", list1.index(45))  # error (없음)

# insert(삽입위치, 삽입할 요소)
list1 = [1, 2, 3]
list1.insert(0, 4)  # 0번 자리에 4 삽입
print("list1 요소 삽입 후 : ", list1)

# remove(제거할 요소)
list1.remove(2)
print("list1 요소 제거 후 : ", list1)

# pop(위치) : 리스트 내 해당 위치 요소 꺼내기
list1 = [1, 2, 3, 4, 5, 6, 7]
print("list1 ", list1)
list1.pop()
print("list1 pop() 후 ", list1)
list1.pop(2)
print("list1 pop(2) 후 ", list1)

# count(x) : list에 포함된 요소 x의 개수
print("list1.count(2) ", list1.count(2))

# extend(x list) : 원래 리스트에 리스트 더하기
list2 = [16, 17, 18]
list1.extend(list2)
print("list1 extend list2 ", list1)

# clear() : 요소 모두 삭제
list1.clear()
print("list1 clear() 후 ", list1)

# 요소 in 리스트명 : 리스트 안에 해당 요소가 있는지 True? False?
fruits = ["딸기", "바나나", "수박", "사과", "참외"]
print("딸기" in fruits)
print("두리안" in fruits)

list1 = []
if list1:
    print("참")
else:
    print("거짓")

# 리스트 요소 출력
for num in enumerate(numbers):
    print(num)  # (0, 273) => (인덱스, 값) 튜플 형태로 반환

for idx, num in enumerate(numbers, start=1):  # index 1부터 시작
    print(idx, num)

# === 실습 ===
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다. 중간고사 점수를 리스트로 생성하고 A 학급의 평균을 구하시오
score = [70, 66, 55, 75, 90, 95, 80, 85, 100, 87]
print("A학급 평균 :", sum(score) / len(score))

# 다음 리스트에서 Apple만 삭제하고 출력하기
fruits = ["Banana", "Apple", "Orange", "Grape"]
fruits.remove("Apple")
print(fruits)
