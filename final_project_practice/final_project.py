import random

def get_user_choice():
    user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
    return user_choice

def get_computer_choice():
    choices = ['가위', '바위', '보']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "무승부"
    elif (user_choice == '가위' and computer_choice == '보') or \
         (user_choice == '바위' and computer_choice == '가위') or \
         (user_choice == '보' and computer_choice == '바위'):
        return "사용자 승리!"
    else:
        return "컴퓨터 승리!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"사용자: {user_choice}")
    print(f"컴퓨터: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

print("가위바위보 게임을 시작합니다!")
play_game()