import math

# Constants
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Initialize the board
board = [[EMPTY for _ in range(3)] for _ in range(3)]


def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def is_draw(board):
    return all(cell != EMPTY for row in board for cell in row)


def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]


def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, AI):
        return 10 - depth
    if is_winner(board, HUMAN):
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = AI
            score = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = EMPTY
            max_eval = max(max_eval, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = HUMAN
            score = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = EMPTY
            min_eval = min(min_eval, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_eval


def best_move(board):
    best_score = -math.inf
    move = None
    for (i, j) in get_available_moves(board):
        board[i][j] = AI
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[i][j] = EMPTY
        if score > best_score:
            best_score = score
            move = (i, j)
    return move


def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X'. The AI is 'O'.")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                move = input("Enter your move (row and column from 0 to 2, e.g., 0 2): ")
                row, col = map(int, move.split())
                if board[row][col] == EMPTY:
                    board[row][col] = HUMAN
                    break
                else:
                    print("Cell already taken. Try again.")
            except:
                print("Invalid input. Use format: row col (e.g., 1 2)")
        print_board(board)

        if is_winner(board, HUMAN):
            print("Congratulations! You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        i, j = best_move(board)
        board[i][j] = AI
        print_board(board)

        if is_winner(board, AI):
            print("AI wins! Better luck next time.")
            break
        elif is_draw(board):
            print("It's a draw!")
            break


# Run the game
if __name__ == "__main__":
    play_game()
