import random # random 모듈 생성

def generate_secret_code(): # generate_secret_code 함수는 0부터 9까지의 난수로 이루어진 4자리의 비밀 코드를 생성
    return [random.randint(0, 9) for _ in range(4)] # 'random.randint(0, 9)'는 0부터 9까지의 랜덤한 정수를 생성하는 함수 / 이를 4번 반복하여 리스트를 생성

def get_user_guess(): # get_user_guess 함수는 사용자로부터 4자리의 숫자를 입력받음.
    while True:
        user_input = input("4개의 숫자를 입력하세요 (0부터 9까지): ")
        if len(user_input) != 4 or not user_input.isdigit(): # 입력이 유효하지 않으면 사용자에게 다시 입력하라는 메시지를 표시
            print("올바른 형식으로 입력하세요.")
        else: # 유효한 입력이면 숫자를 리스트로 변환하여 반환
            return [int(digit) for digit in user_input]

def evaluate_guess(secret_code, user_guess): # evaluate_guess 함수는 비밀 코드와 사용자의 추측을 비교하여 정답의 위치와 숫자를 평가
    correct_positions = sum(a == b for a, b in zip(secret_code, user_guess)) # zip(secret_code, user_guess)는 비밀 코드와 사용자의 추측을 같은 인덱스끼리 묶어주는 역할
    # sum(a == b for a, b in ...)는 두 리스트에서 같은 위치에 있는 숫자가 같은지를 확인하고, 그 결과의 합을 구함.
    correct_numbers = sum(min(secret_code.count(digit), user_guess.count(digit)) for digit in set(user_guess))
    # set(user_guess)는 사용자의 추측에서 중복된 숫자를 제거
    # min(secret_code.count(digit), user_guess.count(digit))는 해당 숫자가 비밀 코드와 사용자의 추측에서 각각 몇 번 나타나는지 중 작은 값을 선택
    return correct_positions, correct_numbers - correct_positions

def play_game(): # play_game 함수는 게임을 실행하는 함수
    secret_code = generate_secret_code() # generate_secret_code를 호출하여 비밀 코드를 생성
    attempts = 0 # 사용자의 시도 횟수를 저장하는 attempts 변수를 초기화

    while True: # 무한 반복문을 통해 사용자의 추측을 받고, 맞춘 경우에는 몇 번 시도 후에 맞췄는지를 출력하고 게임을 종료
        user_guess = get_user_guess()
        attempts += 1

        correct_positions, correct_numbers = evaluate_guess(secret_code, user_guess)

        if correct_positions == 4:
            print(f"축하합니다! {attempts}번만에 정답을 맞추셨습니다.")
            break
        else:
            print(f"정답 위치: {correct_positions}, 정답 숫자 (위치 미포함): {correct_numbers}")

print("다빈치 코드 게임을 시작합니다!")
play_game()