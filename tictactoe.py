import copy

# Tic-Tac-Toe board represented as a 2D list
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def print_board():
    for row in range(3):
        for col in range(3):
            if board[row][col] == -1:
                print("O", end = " ")
            elif board[row][col] == 1:
                print("X", end = " ")
            else:
                print(".", end = " ")
        print()

def check_winner():
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != 0:
            return board[row][0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    # Check for tie
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return 0
    return None

def minimax(board, player, depth):
    winner = check_winner()
    if winner != 0:
        return winner
    if depth == 9:
        return 0
    best_score = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = player
                score = -minimax(board, -player, depth + 1)
                board[row][col] = 0
                if best_score is None or score > best_score:
                    best_score = score
    return best_score

def find_best_move():
    best_score = None
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = 1
                score = -minimax(board, -1, 0)
                board[row][col] = 0
                if best_score is None or score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

if __name__ == "__main__":
    while True:
        print_board()
        # User move
        print("Your turn user!")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != 0:
            print("spot already taken, please choose another spot")
            continue
        board[row][col] = -1
        # AI move
        print("AI's turn!")
        row, col = find_best_move()
        board[row][col] = 1
        print_board()
        winner = check_winner()
        if winner is not None:
            if winner == -1:
                print("You win!")
            elif winner == 1:
                print("AI wins!")
            else:
                print("Tie!")
            break