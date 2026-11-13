# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 15 - Unbeatable Tic-Tac-Toe (PythonLife)

What it does : play X against a computer that uses the minimax algorithm
               (it never loses!).
Concepts     : lists, recursion, minimax decision making.
Run          : python 15_tic_tac_toe.py       (add --demo for a sample run)
"""
from pythonlife import run, ask

LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def winner(board):
    for a, b, c in LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def free_cells(board):
    return [i for i, v in enumerate(board) if v == " "]


def minimax(board, turn, me):
    """+1 if `me` wins, -1 if opponent wins, 0 draw (with best play)."""
    w = winner(board)
    if w:
        return 1 if w == me else -1
    cells = free_cells(board)
    if not cells:
        return 0
    other = "O" if turn == "X" else "X"
    scores = []
    for i in cells:
        board[i] = turn
        scores.append(minimax(board, other, me))
        board[i] = " "
    return max(scores) if turn == me else min(scores)


def best_move(board, me):
    cells = free_cells(board)
    if len(cells) == 9:
        return 4                                   # centre: instant first move
    other = "O" if me == "X" else "X"
    best, best_score = cells[0], -2
    for i in cells:
        board[i] = me
        score = minimax(board, other, me)
        board[i] = " "
        if score > best_score:
            best, best_score = i, score
    return best


def draw(board):
    rows = [" | ".join(board[r * 3:r * 3 + 3]) for r in range(3)]
    print("\n" + "\n---------\n".join(rows) + "\n")


def main():
    board = [" "] * 9
    print("You are X. Cells are numbered 1-9 (left to right, top to bottom).")
    turn = "X"
    while not winner(board) and free_cells(board):
        draw(board)
        if turn == "X":
            raw = ask("Your move (1-9): ")
            if raw.isdigit() and 1 <= int(raw) <= 9 and board[int(raw) - 1] == " ":
                board[int(raw) - 1] = "X"
            else:
                print("  Invalid move.")
                continue
        else:
            board[best_move(board, "O")] = "O"
        turn = "O" if turn == "X" else "X"
    draw(board)
    print(f"{winner(board)} wins!" if winner(board) else "It's a draw!")


def demo():
    board, turn = [" "] * 9, "X"
    while not winner(board) and free_cells(board):
        board[best_move(board, turn)] = turn
        turn = "O" if turn == "X" else "X"
    draw(board)
    print("AI vs AI result:", winner(board) or "draw (perfect play always draws)")


if __name__ == "__main__":
    run(15, "Unbeatable Tic-Tac-Toe", main, demo)
