# 클래스 메소드


class Test:
    # 매개변수에 self가 없는 경우, 클래스 메소드 => 객체명.메소드명 이 아닌 클래스명.클래스메소드명 으로 호출해야 함
    def function1():
        print("function1 호출")

    # 매개변수에 self가 있는 경우, 객체명.메소드명 으로 호출
    def function2(self):
        print("function2 호출")


obj1 = Test()
# 매개변수로 self 필요
# obj1.function1()  # TypeError : Test.function1() takes 0 positional arguments but 1 was given
Test.function1()
obj1.function2()

# 생성자 오버로딩 => X
# 생성자를 여러 개 만들 수 없기 때문에 매개변수에 초기값 설정해줘야 함
class UserInfo:
    """
    UserInfo Class
    Author : 김모씨
    Date : 2022-05-26
    Description : 클래스 작성법
    """

    user_cnt = 0  # 클래스 변수

    # default 생성자
    def __init__(self, name, age, email=None) -> None:
        self.name = name
        self.age = age
        self.email = email
        UserInfo.user_cnt += 1  # 클래스 변수 : static과 같은 개념

    def user_info(self):
        return "name : {}, age : {}".format(self.name, self.age)

    def __del_(self):
        UserInfo.user_cnt -= 1


user1 = UserInfo("김땡땡", 30)  # 인자로 email 넘기지 않으면 Error
print(user1.user_info())

user2 = UserInfo("박모씨", 30, "park@naver.com")
print(user2.user_info())
