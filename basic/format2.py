# format() : 중괄호를 사용해 자리를 잡아두고 나중에 삽입
# print("{}".format(n))

print("{} and {}".format('You', 'Me')) # You and Me
print("{0} and {1} and {0}".format('You', 'Me')) # You and Me and You

print("{var1} and {var2}".format(var1='You', var2='Me')) # You and Me
print("I ate {number} apples. so I was sick for {day} days".format(number = 10, day=3))
print("I ate {0} apples. so I was sick for {day} days".format(10, day=3))

# 5d, 4.2f와 같이 key 값을 반드시 넣어줘야 함
print('Test1 : {0:5d}, Price : {1:4.2f}'.format(776, 6534.123))
print('Test1 : {a:5d}, Price : {b:4.2f}'.format(a=776, b=6534.123))