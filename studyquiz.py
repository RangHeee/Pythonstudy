# 예제 220
# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라.
# 단 if 문을 사용해서 수를 비교하라.

def print_max(a, b, c):
    max_num = a
    if b > a:
        max_num = b
        if c > b:
            max_num = c
    print(max_num)

print_max(23,45,65)


# 예제 234
# 숫자로 구성된 하나의 리스트를 입력받아,
# 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.

def pickup_even(items):
    results = []
    for i in items:
        if i%2 == 0:
            results.append(i)
    return results
    
R = pickup_even([3,4,5,6,7,8])
print(R)


def pickup_even(items):
    return [i for i in items if i%2 == 0]

R = pickup_even([3,4,5,6,7,8])
print(R)


# 예제 126
# 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다.
# 예를 들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.
# 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라.

# pust_num = input("우편번호 : ")
# 우편번호 = input("우편번호: ")
# 우편번호 = 우편번호[:3]
# if 우편번호 in ["010", "011", "012"]:
#     print("강북구")
# elif 우편번호 in ["014", "015", "016"]:
#     print("도봉구")
# else:
#     print("노원구")


# 예제 190
# 리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]

def hamsu(apart):
    for floor in apart:
        for ho in floor:
            print(ho, "호")
    print("-" * 5)

hamsu(apart)

print(apart[1][0])
    

# 예제 210
# 아래 코드의 실행 결과를 예측하라.
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

# 1. 본인의 관심 분야의 클래스를 정의해보기
# - 생성자 및 다양한 메서드 추가
# 2. 여러 객체를 생성하기
# 3. 1번에서 정의한 클래스를 상속받는 새로운 클래스를 정의해보기

from random import *

class marble:
    def __init__(self, name, num1, num2):
        self.name = name
        self.num1 = num1
        self.num2 = num2
        print("{0} player가 {1}, {2}를 출력했습니다.".format(self.name, self.num1, self.num2))

player1 = marble("랑희", 1, 3)





# 코딩도장 추천 많은 Lv1 문제
# Multiples of 3 and 5
# 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
# 1000미만의 자연수에서 3,5의 배수의 총합을 구하라.

# [정답]
result = 0
for n in range(1, 1000):
    if n % 3 == 0:
        result += n
    if n % 5 == 0:
        result += n
print(result)


# [정답 2]
sum = 0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        sum+=i
print(sum)



# 1~1000에서 각 수의 개수 구하기
# 예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자

# 10 = 1, 0
# 11 = 1, 1
# 12 = 1, 2
# 13 = 1, 3
# 14 = 1, 4
# 15 = 1, 5

# 그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개

# [정답]
num_list =[]

for str_num in str(range(1,1001)):
    num_list.append(str_num)

for i in range(0,10):
    print(i, ':', num_list.count(str(i)))




# 예제 297 예외처리 및 리스트에 저장
# 문자열로 표현된 PER 값을 실수로 변환한 후 이를 새로운 리스트에 저장해보세요.
# per = ["10.31", "", "8.00"]

# for i in per:
#     print(float(per))


# [정답]
per = ["10.31", "", "8.00"]
new_per = []

for i in per:
    try:
        v = float(i)
    except:
        v = 0
    new_per.append(v)

print(new_per)



# 예제 300 try, except, else, finally 구조 사용해보기
# 파이썬 예외처리는 다음과 같은 구조를 가질 수 있습니다.

# try:
#     실행 코드
# except:
#     예외가 발생했을 때 수행할 코드
# else:
#     예외가 발생하지 않았을 때 수행할 코드
# finally:
#     예외 발생 여부와 상관없이 항상 수행할 코드

# 아래의 코드에 대해서 예외처리를 사용하고 try, except, else, finally에 적당한 코드를 작성해봅시다.
# else와 finally는 적당한 문구를 print하시면 됩니다.

# per = ["10.31", "", "8.00"]

# for i in per:
#     print(float(per))


# [정답]
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")