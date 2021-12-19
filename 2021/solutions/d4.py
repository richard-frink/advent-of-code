import pandas as pd


def read_input():
    lines = []
    with open('../inputs/input4.txt') as file:
        for line in file:
            line = line.rstrip().lstrip().replace("\n", "").replace("  ", " ")
            if line == "":
                continue
            lines.append(line)
    drawing_numbers = lines[0].split(",")
    boards = []
    board = []
    for line in lines[1:]:
        if len(board) < 5:
            row = []
            for num in line.split(" "):
                row.append([num, False])
            board.append(row)
        else:
            boards.append(board)
            row = []
            for num in line.split(" "):
                row.append([num, False])
            board = [row]
    boards.append(board) # add the final board
    return drawing_numbers, boards

def winning_board(boards):
    for board in boards:
        for r in range(5): # for each row, see if they are all true
            if all(num[1] == True for num in board[r]):
                return board
        # no row wins, now to check columns
        for c in range(5):
            for r in range(5):
                if board[r][c][1] == False:
                    break
                if r == 4: # we hit the final row and it was still True
                    return board
    return None

def solve1(drawing_numbers, boards):
    winner = None
    winning_draw = -1
    for num in drawing_numbers:
        for board in boards:
            for r in range(5):
                for c in range(5):
                    if board[r][c][0] == num:
                        board[r][c][1] = True
        winner = winning_board(boards)
        if winner is not None:
            winning_draw = num
            break
    sum = 0
    print(winner)
    for r in range(5):
        for c in range(5):
            if not winner[r][c][1]:
                sum += int(winner[r][c][0])
    print(int(sum)*int(winning_draw))


def solve2(drawing_numbers, boards):
    last_winner = None
    winning_draw = -1
    for num in drawing_numbers:
        if last_winner is not None:
            break
        for board in boards:
            for r in range(5):
                for c in range(5):
                    if board[r][c][0] == num:
                        board[r][c][1] = True
        while last_winner is None:
            winner = winning_board(boards)
            if winner is not None:
                if len(boards) == 1:
                    last_winner = winner
                    winning_draw = num
                    break
                boards.remove(winner)
            else:
                break
    sum = 0
    for r in range(5):
        for c in range(5):
            if last_winner is not None:
                if not last_winner[r][c][1]:
                    sum += int(last_winner[r][c][0])
    print(int(sum)*int(winning_draw))

def main():
    drawing_numbers, boards = read_input()
    solve1(drawing_numbers, boards)
    drawing_numbers, boards = read_input()
    solve2(drawing_numbers, boards)

main()