# 클래스 변수 - 반드시 선언 필요, 클래스명.클래스변수


class UserInfo:
    """
    UserInfo Class
    Author : 김모씨
    Date : 2022-05-26
    Description : 클래스 작성법
    """

    user_cnt = 0  # 클래스 변수

    # default 생성자
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        UserInfo.user_cnt += 1  # 클래스 변수 : static과 같은 개념

    def user_info(self):
        return "name : {}, age : {}".format(self.name, self.age)

    def __del_(self):
        UserInfo.user_cnt -= 1


user1 = UserInfo("김모씨", 26)
user2 = UserInfo("양모씨", 28)

print(user1.user_info())
print(user2.user_info())

print("현재 생성된 User {}명".format(UserInfo.user_cnt))

# 객체 삭제
del user1  # __del__ 호출
print("현재 생성된 User {}명".format(UserInfo.user_cnt))
