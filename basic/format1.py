# format() == Java의 printf()와 동일
# %c (문자),  %f (실수), %d (정수), %s (문자열)

print('%d' % 100)
print('%5d' % 100) # 5자리 출력
print('%05d' % 100) # 빈 자리는 0으로 채우기

print('%s' % 'hi') # hi
print('%5s' % 'hi') #    hi

print('%8.2f' % 12.21) #    12.21
print('%-8.2f' % 12.21) # 12.21
print('%-8.2f' % 12.2134567) #12.21

print('I eat %d apples' % 3) # I eat 3 apples
print('I eat %s apples' % 3) # I eat 3 apples

number = 4
print('I eat %d apples' % number) # I eat 4 apples
print('I eat', number, 'apples') # I eat 4 apples

# 2개 이상인 경우 괄호로 묶어주기
print('%d : %s' % (1, '김모씨'))
print('%d : %s - %f' % (2, '양모씨', 93.2))
print('Test1 : %5d Price : %r.2f'  % (776,5634.123))

print('I eat %s apples' % 3)
print('I eat %s apples' % 3.156)
print('I eat %s apples' % '3')

print('Error is %d%%' % 98)