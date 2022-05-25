# List Comprehension : 리스트를 편하게 생성하고 사용

# 리스트 생성 1 ~ 100
numbers = []
for n in range(1, 101):
    numbers.append(n)
print(numbers)

numbers = list(range(1, 101))
print(numbers)

numbers2 = [n for n in range(1, 101)]
print(numbers2)

list1 = ["갑", "을", "병", "정"]
for l in list1:
    if l != "정":
        print(l, end=" ")
print([l for l in list1 if l != "정"])

# 1 ~ 100 중에서 홀수만 출력
list1 = [n for n in range(1, 101) if n % 2 == 1]
print(list1)

# 5글자 이상의 단어만 출력
list2 = ["nice", "study", "python", "anaconda", "abe"]
print([word for word in list2 if len(word) >= 5])

# 소문자만 출력
list3 = ["A", "b", "C", "d", "E", "f", "z"]
print([al for al in list3 if al.islower])

# 다음 리스트를 각 요소에 x2 한 후 출력
list4 = [1, 2, 3, 4]
print([x * 2 for x in list4])
