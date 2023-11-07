import random

def generate_secret_code():
    return [random.randint(0, 9) for _ in range(4)]

def get_user_guess():
    while True:
        user_input = input("4개의 숫자를 입력하세요 (0부터 9까지): ")
        if len(user_input) != 4 or not user_input.isdigit():
            print("올바른 형식으로 입력하세요.")
        else:
            return [int(digit) for digit in user_input]

def evaluate_guess(secret_code, user_guess):
    correct_positions = sum(a == b for a, b in zip(secret_code, user_guess))
    correct_numbers = sum(min(secret_code.count(digit), user_guess.count(digit)) for digit in set(user_guess))
    return correct_positions, correct_numbers - correct_positions

def play_game():
    secret_code = generate_secret_code()
    attempts = 0

    while True:
        user_guess = get_user_guess()
        attempts += 1

        correct_positions, correct_numbers = evaluate_guess(secret_code, user_guess)

        if correct_positions == 4:
            print(f"축하합니다! {attempts}번만에 정답을 맞추셨습니다.")
            break
        else:
            print(f"정답 위치: {correct_positions}, 정답 숫자 (위치 미포함): {correct_numbers}")

if __name__ == "__main__":
    print("다빈치 코드 게임을 시작합니다!")
    play_game()