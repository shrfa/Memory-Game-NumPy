import numpy as np
import time

board = np.zeros((4, 4), dtype=int)
numbers = np.random.choice(range(1, 9), size=8, replace=False)
pairs = np.repeat(numbers, 2)
np.random.shuffle(pairs)
board = np.reshape(pairs, (4, 4))


def display_board(board):
    for row in board:
        print("_|_".join(str(cell) if cell != 0 else "_" for cell in row))


def hide_numbers(board, delay):
    time.sleep(delay)
    indices = np.where(board != -1)
    board[indices] = 0
    for row in board:
        print("_|_".join(str(cell) if cell != 0 else "_" for cell in row))


def play_turn(board, cells):
    row1, col1, row2, col2 = cells
    if board[row1][col1] == board[row2][col2]:
        board[row1][col1] = board[row2][col2] = -1
        return True
    else:
        return False


score = 0
selected_cells = set()
display_board(board)
while True:
    print("________________________________")
    hide_numbers(board, delay=5)
    print(f"Score: {score}")
    cells = tuple(
        map(
            int,
            input(
                "Enter the row and column of the first cell followed by the row and column of the second cell, separated by spaces: "
            ).split(),
        )
    )
    if cells in selected_cells:
        print("You can't choose what you've chosen before.")
        continue
    else:
        selected_cells.add(cells)
        if play_turn(board, cells):
            score += 1
        else:
            break

    if np.count_nonzero(board != -1) == 0:
        break

print(f"Game over! Final score: {score}")
