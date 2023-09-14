# def solution(my_string, n):
#     answer = ''
#     for i in my_string:
#         answer += i * n
#     return answer

# print(solution)


# name = '강민석'
# new_name = ''
# for char in name:
#     new_name += char * 3
# print(new_name)




import random
lotto = []

# 아래에 코딩하세요
# 1. for문 or while문 반드시 사용하기
# 2. random.randint() 활용하기

# 랜덤 로또 번호 출력
# print(lotto)

# from random import *
# for i in range(6):
#     num = randint(1, 45)
#     if num not in lotto: # 중복 안되게
#         lotto.append(num)

# print(lotto)


my_lotto = [13,23,33,43,44,45]

# 각자 좋아하는 숫자로 바꿔도 됩니다.
# 아래에 코딩하세요
# 1. set 자료형 활용하기
# 2. while문 활용하기

# 결과 예시
# 1개 : 낙첨
# 3개 : 당첨

from random import *
my_lotto = [13,23,33,43,44,45]
for i in range(6):
    num = randint(1, 45)
    if num not in lotto: # 중복 안되게
        lotto.append(num)

print(lotto)

while true: