def print_board(board):
    print()
    print(board)
    print("-------------")
    for row in board:
        print("|", row[0], "|", row[1], "|", row[2], "|")
        print("-------------")
    print()

def check_win(board, player):
    win_conditions = [
        # rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_conditions

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_move(player):
    while True:
        try:
            move = input(f"Тоглогч {player}, мөр,баганаа оруулна уу! (e.g. 1,2): ")
            row, col = move.split(",")
            row = int(row.strip()) - 1
            col = int(col.strip()) - 1
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Мөр болон багана 1-3 хооронд байх ёстой.")
        except ValueError:
            print("Заваал мөр болон багана дундаа таслалтай байх ёстой.")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not game_over:
        row, col = get_move(current_player)

        if board[row][col] != " ":
            print("Энэ нүх дүүрсэн байна. Дахин оролдоно уу.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"Тоглогч {current_player} яллаа!")
            game_over = True
        elif check_tie(board):
            print("Тэнцлээ!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
