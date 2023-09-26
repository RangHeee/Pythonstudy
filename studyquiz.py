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

pust_num = input("우편번호 : ")
