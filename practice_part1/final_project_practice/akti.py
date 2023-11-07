def print_board(board): #게임보드의 현재 상태를 보여주는 기능으로 보드의 행과 열을 반복하고 
                        #구분자로 인쇄하여 게임보드를 시각적으로 표현합니다.
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_who_is_the_winner(board, player): #We check three conditions of the winner 
                        #이 함수는 승리 조합을 위해 행, 열, 대각선을 조사하여 현재 플레이어가 승리했는지 확인함
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def the_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def main(): #The main function 게임 제어하는 주요 부분.
#게임 보드를 빈 셀이 있는 3x3 그리드로 초기화하고 시작 플레이어를  - "X"
#이것은 선수들이 교대로 움직임을 만들고 승자와 무승부를 확인하는 루프로 들어갑니다.
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)
        row, col = map(int, input(f"Player {player}, enter row and column (two numbers like 1 and 2): ").split())

        if board[row - 1][col - 1] == " ": #We check if the cell is empty
            board[row - 1][col - 1] = player # We put X or O
        else:
            print("Cell already occupied. Try again.")
            continue

        if check_who_is_the_winner(board, player): #If it is true
            print_board(board)
            print(f"Player {player} wins! Congratulations!")
            break

        if the_board_full(board): # No one wins  #이 함수는 게임보드가 가득 차 있는지 확인한다. 
                                           #승리한 플레이어가 없으므로 무승부를 나타낸다.
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    main()