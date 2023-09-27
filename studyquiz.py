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

class marble:
    def __init__(self, name, num1, num2)
        self.name = name
        self.num1 = num1
        self.num2 = num2
        print("{0} player가 {1}, {2}를 출력했습니다.".format(self.name, self.num1, self.num2))

